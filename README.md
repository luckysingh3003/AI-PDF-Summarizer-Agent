# 📄 AI PDF Summarizer Agent

## Overview

AI PDF Summarizer Agent is an AI-powered application that helps users quickly understand lengthy PDF documents. Users can upload a PDF, and the application automatically generates:

- 📝 Summary
- ⭐ Key Points
- ❓ Quiz Questions

The project is built using **Python**, **Streamlit**, and **Meta Llama 3.1 (via Hugging Face Inference API)**.

---

# Problem Statement

Reading long PDF documents is time-consuming. Students, researchers, and professionals often need to extract the most important information quickly without reading every page.

This project solves that problem by automatically summarizing documents and generating learning material.

---

# Solution

The AI PDF Summarizer Agent follows these steps:

1. Upload a PDF.
2. Extract text from the document.
3. Send the extracted text to the Llama 3.1 model.
4. Generate:
   - Summary
   - Key Points
   - Quiz Questions
5. Display results in an easy-to-use interface.

---

# Features

- 📄 PDF Upload
- 📝 AI Summary
- ⭐ Key Point Extraction
- ❓ AI Quiz Generation
- ⚡ Simple Streamlit Interface

---

# Architecture

```text
                User
                  │
                  ▼
          Upload PDF (Streamlit)
                  │
                  ▼
          PDF Text Extraction
              (PyPDF2)
                  │
                  ▼
      Hugging Face Inference API
         (Meta Llama 3.1 8B)
                  │
                  ▼
    ┌─────────────┼─────────────┐
    ▼             ▼             ▼
 Summary      Key Points      Quiz
    └─────────────┼─────────────┘
                  ▼
          Results Displayed
```

---

# Tech Stack

- Python
- Streamlit
- Hugging Face Inference API
- Meta Llama 3.1 8B Instruct
- PyPDF2

---

# Project Structure

```
AI-PDF-Summarizer-Agent/
│
├── app.py
├── requirements.txt
├── README.md
└── .streamlit/
```
