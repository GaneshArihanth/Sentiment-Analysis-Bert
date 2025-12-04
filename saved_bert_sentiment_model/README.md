---
license: mit
datasets:
- fancyzhx/amazon_polarity
language:
- en
base_model:
- google-bert/bert-base-uncased
pipeline_tag: text-classification
tags:
- sentiment-analysis
- amazon-reviews
- bert
- huggingface
- fine-tuned-model

---

# BERT Sentiment Analysis on Amazon Polarity:

This model fine-tunes the `bert-base-uncased` model from Google on the [Amazon Polarity](https://huggingface.co/datasets/fancyzhx/amazon_polarity) dataset to classify customer reviews into **positive** or **negative** sentiment.

---

## Model Details:-

### Model Description:

- **Developed by:** Ganesh Arihanth  
- **Finetuned from model:** `google-bert/bert-base-uncased`  
- **Language(s):** English  
- **License:** MIT  
- **Model type:** Transformer-based sentiment classifier  
- **Dataset used:** `fancyzhx/amazon_polarity`  
- **Pipeline type:** `text-classification`

### Model Sources:

- **Repository:** [GitHub Repo](https://github.com/yourusername/sentiment-analysis-bert-amazon)  
- **Dataset:** [Amazon Polarity](https://huggingface.co/datasets/fancyzhx/amazon_polarity)  
- **Base model:** [BERT base uncased](https://huggingface.co/bert-base-uncased)

### Results:

| Metric     | Value    |
|------------|----------|
| Accuracy   | 96.5%    |
| F1 Score   | 96.36%   |
| Precision  | ~96.3%   |
| Recall     | ~96.4%   |

---

## Uses:-

### Direct Use:

- Binary sentiment classification (positive/negative) of product reviews  
- Customer feedback analysis  
- E-commerce analytics dashboards

### Downstream Use:

- Chatbots or virtual assistants for feedback and understanding  
- Review filtering systems  
- Business intelligence tools for automated sentiment insights

### Out-of-Scope Use:

- Not suitable for non-English text without re-training  
- Not suitable for detecting sarcasm or highly nuanced sentiment  
- Not trained for offensive content detection

---

## Bias, Risks, and Limitations:-

- Trained only on Amazon product reviews; may not generalise well to other domains  
- Risk of overfitting to Amazon-specific language  
- May perform poorly on concise, ambiguous, or sarcastic reviews

## Recommendations:-

- Evaluate on your domain-specific test set before deployment  
- Retrain or fine-tune further if accuracy is low on your data

---

## How to Use:-

```python
import torch
from transformers import BertTokenizerFast, BertForSequenceClassification

# Set the device (use GPU if available)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")

# Load the saved model and tokenizer
model_path = "GaneshArihanth/bert-amazon-sentiment"  # Change to your actual HF repo path
tokenizer = BertTokenizerFast.from_pretrained(model_path)
model = BertForSequenceClassification.from_pretrained(model_path)
model.to(device)
model.eval()

# Function to predict sentiment
def predict_sentiment(text):
    inputs = tokenizer(
        text,
        padding="max_length",
        truncation=True,
        max_length=128,
        return_tensors="pt"
    )
    input_ids = inputs["input_ids"].to(device)
    attention_mask = inputs["attention_mask"].to(device)

    with torch.no_grad():
        outputs = model(input_ids, attention_mask=attention_mask)
        logits = outputs.logits
        prediction = torch.argmax(logits, dim=-1).item()

    sentiment = "Positive 😊" if prediction == 1 else "Negative 😖"
    return sentiment

# Example usage
while True:
    user_input = input("Enter a review (or 'exit' to quit): ")
    if user_input.lower() == "exit":
        break
    result = predict_sentiment(user_input)
    print(f"Predicted Sentiment: {result}")

```

---

## Training Procedure:-

- **Hardware:** NVIDIA RTX 3060 (12GB VRAM)
- **Batch Size:** 64
- **Epochs:** 2
- **Optimizer:** AdamW
- **Learning Rate:** 2e-5
- **Max Sequence Length:** 512
- **Mixed Precision:** Enabled (FP16)
- **Framework:** PyTorch + Hugging Face Transformers

---

## Technical Specifications:-
### Model Architecture
- **Model:** BERT (base, uncased)

- **Parameters:** 110M

- **Layers:** 12

- **Heads:** 12

- **Hidden Size:** 768

- **Task Objective:** Binary classification using [CLS] token

### Infrastructure
- **Environment:** Python 3.10+, PyTorch, Hugging Face Transformers

- **Device:** RTX 3060 with CUDA

---

