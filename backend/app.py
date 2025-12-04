from flask import Flask, request, jsonify
from flask_cors import CORS
import torch
from transformers import BertTokenizerFast, BertForSequenceClassification
import os

app = Flask(__name__)
CORS(app)

# Set the device
device = "mps" if torch.backends.mps.is_available() else "cpu"
print(f"Using device: {device}")

# Load the saved model and tokenizer
# Assuming the model is in the parent directory as per the structure
# Load the saved model and tokenizer
# Use absolute path or path relative to this script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "..", "saved_bert_sentiment_model3final")


try:
    print("Loading model...")
    loaded_tokenizer = BertTokenizerFast.from_pretrained(MODEL_PATH)
    loaded_model = BertForSequenceClassification.from_pretrained(MODEL_PATH)
    loaded_model.to(device)
    loaded_model.eval()
    print("Model loaded successfully!")
except Exception as e:
    print(f"Error loading model: {e}")
    # We might want to exit if model fails to load, but for now let's just print
    pass

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
    app.run(debug=True, port=5001)
