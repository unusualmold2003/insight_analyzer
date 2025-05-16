# 🧠 Gemini Insight Synthesizer

A FastAPI-based web tool powered by Google's Gemini (Generative AI) that analyzes free-form survey responses and synthesizes them into structured insights with sentiment tagging.

![Gemini Insight Synthesizer Screenshot](https://img.shields.io/badge/Powered%20By-Google%20Gemini-blue?logo=google)

---

## ✨ Features

- AI-powered analysis of open-text survey responses  
- Groups responses into **3 key themes**  
- Extracts **representative quotes** and **sentiment** (positive/neutral/negative)  
- Frontend UI with dynamic result cards  
- Easy to deploy via Vercel, local server, or any cloud provider

---

## 🚀 Live Demo

Please visit https://insight-analyzer.vercel.app/ for the Live Demo!

---

## 📦 Requirements

- Python 3.9+
- Google Gemini API Key
- FastAPI
- Uvicorn
- `google-generativeai` Python SDK
- python-dotenv

---

## 🔧 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/gemini-insight-synthesizer.git
cd gemini-insight-synthesizer
```
### 2. Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```
### 3. Install dependencies

```bash
pip install -r requirements.txt
```
Example requirements.txt:

```bash
fastapi
uvicorn
python-dotenv
google-generativeai
```

### 4. Set up your Gemini API Key

Create a .env file in the root directory:
```bash
GEMINI_API_KEY=your_google_gemini_api_key_here
```

You can get your API key from: https://makersuite.google.com/app/apikey

▶️ Run Locally
```bash
uvicorn main:app --reload
```
Then open your browser and visit:
```bash
http://localhost:8000
```

## 🖼️ Folder Structure

```text
.
├── static/
│   └── index.html         # Frontend UI
├── main.py                # FastAPI backend
├── .env                   # Your Gemini API key
├── requirements.txt
└── vercel.json            # Vercel config (for deployment)
```

## 🌐 Deploying on Vercel


    Push this repo to GitHub

    Go to https://vercel.com

    Import your repo

    Set the project as a Python backend (@vercel/python)

    Add your GEMINI_API_KEY to Environment Variables

    Done 🎉

    Your routes are configured via vercel.json.


## 📋 Sample Prompt Template

```bash
You are an insight synthesizer...

Survey Responses:
[
  "The dashboard is clean and simple",
  "I want more control over filters",
  "Privacy concerns are real"
]
```
```
Output (JSON):
[
  {
    "theme": "Usability",
    "quotes": ["The dashboard is clean and simple"],
    "sentiment": "positive"
  },
 
]
```
