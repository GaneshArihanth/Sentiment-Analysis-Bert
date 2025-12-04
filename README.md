# Sentiment Analyzer 🧠

A premium, interactive web application for real-time sentiment analysis. This project leverages a fine-tuned **BERT** model to classify text as **Positive** or **Negative** with high accuracy, wrapped in a modern, aesthetically pleasing React frontend.

---

## 📘 Beginner's Corner: What is this?

If you are new to Machine Learning, welcome! 👋

**What is Sentiment Analysis?**
Imagine you have a super-smart assistant who reads a sentence and instantly tells you if the person is happy, angry, or disappointed. That is **Sentiment Analysis**. It's widely used by companies to understand customer feedback, monitor social media, and improve products.

**How does it work?**
We don't just look for keywords like "good" or "bad". We use a sophisticated AI model called **BERT** that understands the *context* of a sentence. For example, it knows that "not bad" is actually positive, even though it contains the word "bad".

---

## 🧠 Deep Dive: The BERT Architecture

This project is built on **BERT** (Bidirectional Encoder Representations from Transformers), a revolutionary model developed by Google.

### 1. The Transformer "Engine"
At its core, BERT uses a **Transformer** architecture. Unlike older models that read text from left to right (like humans do), Transformers read the entire sentence at once. This allows the model to understand the relationship between every word simultaneously.

### 2. Bidirectional Context
The "B" in BERT stands for **Bidirectional**.
- **Unidirectional models** read: "The quick brown..." (can't see what's coming next).
- **BERT** reads: "...quick brown fox..." (sees both "quick" and "fox" to understand "brown").
This allows BERT to understand nuance. For example, it can distinguish between a "river **bank**" and a "**bank** account" based on the surrounding words.

### 3. Fine-Tuning
We didn't build BERT from scratch (that takes supercomputers!). We used a technique called **Transfer Learning**:
1.  **Pre-training**: Google trained BERT on massive amounts of text (Wikipedia, Books) to teach it the English language.
2.  **Fine-tuning**: We took this "smart" model and gave it a specific job: "Read these reviews and tell me if they are positive or negative." This is what makes our model specialized for Sentiment Analysis.

---

## 🔭 Project Scope

### Current Capabilities
- **Real-time Analysis**: Instant feedback as you type or submit text.
- **Binary Classification**: accurately identifies **Positive** vs **Negative** sentiment.
- **Confidence Scoring**: Tells you *how sure* the model is about its prediction (e.g., "99.8% confident").
- **Interactive UI**: A high-end user interface that demonstrates how AI can be presented beautifully.

### Future Roadmap
- **Batch Processing**: Upload a CSV file of thousands of reviews for bulk analysis.
- **Multi-Class Sentiment**: Detecting Neutral, Angry, Sad, or Sarcastic tones.
- **History Tracking**: Saving past analyses to a database.
- **API Integration**: Allowing other developers to use this backend as a service.

---

## ✨ Features

### 🚀 Advanced NLP Backend
- **BERT Model**: Utilizes `BertForSequenceClassification` fine-tuned for sentiment analysis.
- **High Performance**: Optimized for fast inference on local machines (supports MPS/CPU).
- **Flask API**: Robust REST API handling prediction requests.
- **CORS Enabled**: Configured to securely handle cross-origin requests from the frontend.

### 🎨 Premium Frontend Experience
- **Interactive DotGrid Background**: A physics-based background where dots react to mouse movements and clicks with inertia and shockwave effects (powered by **GSAP**).
- **Variable Proximity Heading**: The main title dynamically adjusts its font weight and size based on how close your mouse cursor is (powered by **Framer Motion**).
- **ShinyText Effect**: A subtle, premium shimmer animation on the subtitle.
- **Glassmorphism Design**: Modern, frosted-glass UI elements with smooth hover effects and transitions.
- **Dynamic Feedback**: Visual cues for positive (Green) and negative (Red) results, including a confidence confidence bar.

---

## 🛠️ Tech Stack

### Backend
- **Python 3.x**: The programming language for the AI logic.
- **Flask**: A lightweight web framework to create the API.
- **PyTorch**: The deep learning library running the BERT model.
- **Transformers**: Hugging Face's library to easily load and use BERT.

### Frontend
- **React 18**: The library for building the user interface.
- **Vite**: A super-fast tool for building and running the frontend.
- **GSAP & Framer Motion**: Libraries for complex, high-performance animations.
- **CSS3**: Custom styling for the glassmorphism and layout.

---

## 📦 Installation Guide

### Prerequisites
You need these installed on your computer:
- **Python 3.8+**: To run the backend.
- **Node.js 16+**: To run the frontend.

### 1. Backend Setup (The Brain)
This sets up the server that runs the AI model.

1.  Navigate to the backend folder:
    ```bash
    cd backend
    ```
2.  Install the necessary "tools" (libraries) for Python:
    ```bash
    pip install -r requirements.txt
    ```
    *This installs Flask, PyTorch, and Transformers.*

### 2. Frontend Setup (The Face)
This sets up the website you interact with.

1.  Open a new terminal and navigate to the frontend folder:
    ```bash
    cd frontend
    ```
2.  Install the necessary "tools" (packages) for the website:
    ```bash
    npm install
    ```
    *This downloads React, GSAP, and other interface libraries.*

---

## 🚀 Usage

### Step 1: Start the Backend
The backend needs to be running to process your text.
```bash
# In the backend terminal
python app.py
```
*Wait until you see "Running on http://127.0.0.1:5001". This means the brain is awake!*

### Step 2: Start the Frontend
Now start the website.
```bash
# In the frontend terminal
npm run dev
```
*You will see a link like `http://localhost:5173`. Click it to open the app!*

---

## 📡 API Documentation

For developers who want to use the backend programmatically.

### POST `/predict`
Analyzes the sentiment of the provided text.

**Request Body:**
```json
{
  "text": "I love this product!"
}
```

**Response:**
```json
{
  "sentiment": "Positive",
  "confidence": 0.998,
  "label": 1
}
```

---

## 🎨 Customization

### Changing Background Colors
You can customize the `DotGrid` colors in `frontend/src/App.jsx`:
```jsx
<DotGrid
  baseColor="#222244"   // Default subtle color
  activeColor="#646cff" // Hover highlight color
  dotSize={4}           // Size of the dots
/>
```

### Adjusting Animation Speed
Modify the `ShinyText` speed in `frontend/src/App.jsx`:
```jsx
<ShinyText 
  speed={3} // Duration in seconds
/>
```

---

## 📂 Project Structure

```
Sentiment analysis/
├── backend/
│   ├── app.py                 # The API server (Flask)
│   └── requirements.txt       # List of Python libraries needed
├── frontend/
│   ├── src/
│   │   ├── App.jsx            # The main page layout
│   │   ├── DotGrid.jsx        # The background dots animation
│   │   ├── VariableProximity.jsx # The interactive title
│   │   ├── ShinyText.jsx      # The shimmering subtitle
│   │   └── index.css          # Colors and fonts
│   ├── package.json           # List of JavaScript libraries needed
│   └── vite.config.js         # Configuration for the build tool
├── saved_bert_sentiment_model3final/  # The "Brain" (Model files)
└── README.md                  # You are reading this!
```

## 🔧 Troubleshooting

- **Port Conflicts**: The backend runs on port `5001`. If you see an error about the port being in use (common on Macs with AirPlay), you can change it in `backend/app.py`.
- **Model Not Found**: The app needs the `saved_bert_sentiment_model3final` folder. Ensure it's in the main project folder, not inside `backend` or `frontend`.

## 🤝 Contributing

Contributions are welcome! If you have ideas to make the UI cooler or the model smarter, feel free to fork the repo and submit a Pull Request.

## 📝 License

This project is open source and available under the [MIT License](LICENSE).
