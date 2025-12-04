from flask import Flask, request, jsonify
from flask_cors import CORS
import torch
from transformers import BertTokenizerFast, BertForSequenceClassification
import os

app = Flask(__name__)
CORS(app)

# Set the device
device = "cpu" # HF Spaces free tier is CPU only usually, or we can check.
# But for safety and simplicity on free tier, let's stick to CPU or auto-detect but expect CPU.
if torch.cuda.is_available():
    device = "cuda"
elif torch.backends.mps.is_available():
    device = "mps"
else:
    device = "cpu"

print(f"Using device: {device}")

# Load the saved model and tokenizer
# In HF Spaces, we will upload the model files to the root of the repository or a subfolder.
# Let's assume the user uploads the contents of 'saved_bert_sentiment_model3final' to the root of the Space.
# So the path is just "." or specific folder if they upload the folder itself.
# To be safe and organized, let's assume they upload the folder 'model' or just files to root.
# Best practice for manual upload: Upload files to root.
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
    # In a Space, if model fails, the app might crash or just not work.

@app.route('/')
def home():
    return "Sentiment Analysis API is Running!"

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
        # 1 is Positive, 0 is Negative based on the notebook
        sentiment = "Positive" if prediction == 1 else "Negative"
        
        # Calculate confidence (softmax)
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
    # HF Spaces expects the app to run on port 7860
    app.run(debug=False, host='0.0.0.0', port=7860)
