from flask import Flask, request, jsonify
from flask_cors import CORS
import torch
from transformers import BertTokenizerFast, BertForSequenceClassification
import os

# Configure Flask to serve static files from 'dist' folder
app = Flask(__name__, static_folder='dist', static_url_path='/')
CORS(app)

# Set the device
device = "cpu" 
if torch.cuda.is_available():
    device = "cuda"
elif torch.backends.mps.is_available():
    device = "mps"
else:
    device = "cpu"

print(f"Using device: {device}")

# Load the saved model and tokenizer
MODEL_PATH = "." 

try:
    print("Loading model...")
    loaded_tokenizer = BertTokenizerFast.from_pretrained(MODEL_PATH)
    loaded_model = BertForSequenceClassification.from_pretrained(MODEL_PATH)
    loaded_model.to(device)
    loaded_model.eval()
    print("Model loaded successfully!")
except Exception as e:
    print(f"Error loading model: {e}")

@app.route('/')
def home():
    # Serve the React app
    return app.send_static_file('index.html')

@app.route('/<path:path>')
def static_proxy(path):
    # Serve other static files (JS, CSS, etc.)
    return app.send_static_file(path)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    text = data.get('text', '')
    
    if not text:
        return jsonify({'error': 'No text provided'}), 400

    try:
        tokens = loaded_tokenizer(
            text,
            padding="max_length",
            truncation=True,
            max_length=128,
            return_tensors="pt"
        )
        input_ids = tokens["input_ids"].to(device)
        attention_mask = tokens["attention_mask"].to(device)

        with torch.no_grad():
            logits = loaded_model(input_ids, attention_mask=attention_mask).logits
        
        prediction = torch.argmax(logits, dim=1).item()
        sentiment = "Positive" if prediction == 1 else "Negative"
        
        probs = torch.nn.functional.softmax(logits, dim=1)
        confidence = probs[0][prediction].item()

        return jsonify({
            'sentiment': sentiment,
            'confidence': confidence,
            'label': prediction
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=7860)
