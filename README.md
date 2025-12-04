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

## 📦 Installation Guide (Local)

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

### 3. Running Locally
1.  **Start Backend**:
    ```bash
    # In backend folder
    python app.py
    ```
2.  **Start Frontend**:
    ```bash
    # In frontend folder
    npm run dev
    ```
3.  Open the link shown (e.g., `http://localhost:5173`).

---

## ☁️ Deployment Guide (Step-by-Step)

This project uses a **Split Deployment** strategy.
-   **Why?** The BERT model is large (hundreds of MBs). Free frontend hosting (like Vercel) cannot handle this size.
-   **Solution**: We host the "Brain" (Model) on **Hugging Face Spaces** (which offers free CPU hosting for models) and the "Face" (Frontend) on **Vercel** (which is optimized for React).

### Part 1: Deploying the Backend (Hugging Face Spaces)

1.  **Create an Account**: Go to [huggingface.co](https://huggingface.co/) and sign up.
2.  **Create a Space**:
    -   Click on your profile picture -> **New Space**.
    -   **Space Name**: `bert-sentiment-api` (or similar).
    -   **License**: `MIT`.
    -   **SDK**: Select **Docker**.
    -   **Docker Template**: Select **Blank**.
    -   **Space Hardware**: Keep it as **CPU Basic (Free)**.
    -   Click **Create Space**.
3.  **Upload Files**:
    -   Go to the **Files** tab of your new Space.
    -   Click **Add file** -> **Upload files**.
    -   **Drag and drop** the following files from your local `hf_space` folder:
        -   `app.py`
        -   `requirements.txt`
        -   `Dockerfile`
    -   **CRITICAL**: Drag and drop **ALL FILES** from your local `saved_bert_sentiment_model` folder into the root.
        -   *Do not upload the folder itself, upload the files INSIDE it.*
        -   You should see `config.json`, `pytorch_model.bin`, etc., listed right next to `app.py`.
    -   Click **Commit changes to main**.
4.  **Wait for Build**:
    -   The Space will show "Building". This might take 2-5 minutes.
    -   When it says **Running**, your API is ready!
5.  **Get the API URL**:
    -   Click the **three dots** (⋮) in the top right -> **Embed this space**.
    -   Copy the **Direct URL**. It looks like: `https://username-space.hf.space`.

### Part 2: Deploying the Frontend (Vercel)

1.  **Push to GitHub**:
    -   Ensure your project is pushed to a GitHub repository.
2.  **Import to Vercel**:
    -   Go to [vercel.com](https://vercel.com) and log in.
    -   Click **Add New...** -> **Project**.
    -   Select your GitHub repository.
3.  **Configure Project**:
    -   **Framework Preset**: Select **Vite**.
    -   **Root Directory**: Click Edit and select `frontend`.
4.  **Environment Variables**:
    -   Expand the **Environment Variables** section.
    -   **Key**: `VITE_API_URL`
    -   **Value**: Paste the **Direct URL** from Hugging Face (Part 1, Step 5).
        -   *Example*: `https://ganesharihanth-bert-sentiment-api.hf.space`
        -   *Note*: Remove any trailing slash `/` at the end.
5.  **Deploy**:
    -   Click **Deploy**.
    -   Wait for the confetti! 🎉

### Part 3: Verification
-   Open your Vercel app URL.
-   Type "I am so happy this works!" and click Analyze.
-   If you see "Positive" and a confidence score, everything is connected!

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

## 📂 Project Structure

```
Sentiment analysis/
├── backend/                   # Local Flask API
│   ├── app.py
│   └── requirements.txt
├── frontend/                  # React Frontend
│   ├── src/
│   │   ├── App.jsx            # Main Logic
│   │   └── ...
│   └── package.json
├── hf_space/                  # Deployment files for Hugging Face
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
├── saved_bert_sentiment_model/  # The "Brain" (Model files)
└── README.md                  # You are reading this!
```

## 🤝 Contributing

Contributions are welcome! If you have ideas to make the UI cooler or the model smarter, feel free to fork the repo and submit a Pull Request.

## 📝 License

This project is open source and available under the [MIT License](LICENSE).
