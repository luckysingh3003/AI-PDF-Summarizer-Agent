# 📄 AI PDF Summarizer Agent

An AI-powered PDF Summarizer built with **Python**, **Streamlit**, and **Llama 3.1 (via Hugging Face Inference API)**. Upload any PDF document to instantly generate a concise summary, extract key points, and create an AI-generated quiz.

## 🚀 Live Demo

https://ai-pdf-summarizer-agent-jjgeyrqjhzx5xhuhwya7dt.streamlit.app/

---

## ✨ Features

- 📄 Upload PDF documents
- 📝 Generate concise AI summaries
- ⭐ Extract important key points
- ❓ Automatically generate quizzes
- ⚡ Simple and user-friendly Streamlit interface

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Hugging Face Inference API
- Meta Llama 3.1 8B Instruct
- PyPDF2

---

## 📂 Project Structure

```
AI-PDF-Summarizer-Agent/
│
├── app.py
├── requirements.txt
├── README.md
└── .streamlit/
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/luckysingh3003/AI-PDF-Summarizer-Agent.git
cd AI-PDF-Summarizer-Agent
```

Create virtual environment

```bash
python -m venv .venv
```

Activate virtual environment

### Windows

```bash
.venv\Scripts\activate
```

### macOS/Linux

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

## 🔐 Environment Variables

Create a `.streamlit/secrets.toml` file.

```toml
HF_TOKEN="your_huggingface_api_key"
```

**Never commit your API key to GitHub.** Streamlit Community Cloud provides secure Secrets Management for deployment. :contentReference[oaicite:0]{index=0}

---

## 📸 Screenshots

Add screenshots of:

- Home Page
- PDF Upload
- Generated Summary
- Quiz Generation

---

## 🎥 Demo Video

Add your YouTube (Unlisted) demo video link here.

---

## 🎯 Future Improvements

- Chat with PDF
- Multi-document support
- Flashcard generation
- Multi-language summaries
- Conversation memory
- Export summary as PDF

---

## 👨‍💻 Author

**Lucky Singh**

GitHub: https://github.com/luckysingh3003

---

## ⭐ If you like this project

Please consider giving it a ⭐ on GitHub.
