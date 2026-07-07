import streamlit as st
from huggingface_hub import InferenceClient
from PyPDF2 import PdfReader
import json
import re

st.set_page_config(page_title="PDF Summarizer Agent", layout="wide")

MODEL_ID = "meta-llama/Llama-3.1-8B-Instruct"

st.title("📄 PDF Summarizer Agent")
st.caption("Upload a PDF → get summary, key points, and an auto-generated quiz.")

 
hf_token ="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"
if not hf_token:
    hf_token = st.sidebar.text_input("HuggingFace Token", type="password")

if hf_token:
    client = InferenceClient(token=hf_token)

def call_hf(prompt, max_tokens=5000):
    response = client.chat_completion(
        messages=[{"role": "user", "content": prompt}],
        model=MODEL_ID,
        max_tokens=max_tokens,
    )
    return response.choices[0].message.content

def extract_text(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        t = page.extract_text()
        if t:
            text += t + "\n"
    return text

def get_summary(text):
    prompt = f"""Summarize the following document in 150-200 words, clear and easy to understand:

{text[:8000]}"""
    return call_hf(prompt)

def get_key_points(text):
    prompt = f"""Extract the 6-10 most important points from this document.
Return ONLY a JSON array of strings, no markdown, no explanation, no extra text.

Document:
{text[:8000]}"""
    raw = call_hf(prompt)
    raw = raw.strip().strip("```json").strip("```").strip()
    try:
        return json.loads(raw)
    except:
        return [raw]

def generate_quiz(text, num_q=5):
    prompt = f"""Create a {num_q}-question multiple choice quiz based on this document.
Combine ALL questions into ONE single JSON array — do not output separate arrays.
Return ONLY that one valid JSON array, no markdown, no explanation:
[{{"question": "...", "options": ["...", "...", "...", "..."], "answer": "..."}}]
The "answer" field must be the FULL TEXT of the correct option, not a letter.

Document:
{text[:8000]}"""
    raw = call_hf(prompt, max_tokens=3000)
    raw = raw.strip().strip("```json").strip("```").strip()

    try:
        result = json.loads(raw)
        if isinstance(result, list):
            return result
    except:
        pass

    objects = re.findall(r'\{[^{}]*"question".*?"answer"\s*:\s*"[^"]*"\s*\}', raw, re.DOTALL)
    quiz = []
    for obj_str in objects:
        try:
            quiz.append(json.loads(obj_str))
        except:
            continue
    return quiz

def resolve_correct_text(correct_raw, options):
    correct_raw = correct_raw.strip()
    if correct_raw.upper() in ["A", "B", "C", "D"] and len(correct_raw) == 1:
        idx = ord(correct_raw.upper()) - ord("A")
        if idx < len(options):
            return options[idx]
    return correct_raw

# ---------- MAIN APP ----------
uploaded_file = st.file_uploader("Upload your PDF", type=["pdf"])

if uploaded_file and hf_token:
    if "pdf_text" not in st.session_state or st.session_state.get("last_file") != uploaded_file.name:
        with st.spinner("Extracting text..."):
            st.session_state["pdf_text"] = extract_text(uploaded_file)
            st.session_state["last_file"] = uploaded_file.name

    text = st.session_state["pdf_text"]

    if not text.strip():
        st.error("Couldn't extract text — PDF might be scanned/image-based.")
    else:
        tab1, tab2, tab3 = st.tabs(["📝 Summary", "🔑 Key Points", "🧠 Quiz"])

        with tab1:
            if st.button("Generate Summary"):
                with st.spinner("Summarizing..."):
                    st.write(get_summary(text))

        with tab2:
            if st.button("Extract Key Points"):
                with st.spinner("Extracting key points..."):
                    points = get_key_points(text)
                    for i, p in enumerate(points, 1):
                        st.markdown(f"**{i}.** {p}")

        with tab3:
            num_q = st.slider("Number of questions", 3, 10, 5)
            if st.button("Generate Quiz"):
                with st.spinner("Building quiz..."):
                    st.session_state["quiz"] = generate_quiz(text, num_q)

            if "quiz" in st.session_state and st.session_state["quiz"]:
                answers = {}
                for i, q in enumerate(st.session_state["quiz"]):
                    st.markdown(f"**Q{i+1}. {q['question']}**")
                    answers[i] = st.radio(
                        "", q["options"], key=f"q{i}",
                        index=None, label_visibility="collapsed"
                    )
                    st.divider()

                if st.button("Submit Quiz"):
                    score = 0
                    for i, q in enumerate(st.session_state["quiz"]):
                        selected = answers[i]
                        correct_text = resolve_correct_text(q["answer"], q["options"])
                        if selected is None:
                            st.write(f"Q{i+1}: ⚠️ Not answered")
                            continue
                        is_correct = selected.strip().lower() == correct_text.strip().lower()
                        score += is_correct
                        mark = "✅" if is_correct else f"❌ (Correct: {correct_text})"
                        st.write(f"Q{i+1}: {mark}")
                    st.success(f"🎯 Final Score: {score}/{len(st.session_state['quiz'])}")
elif not hf_token:
    st.info("👈 Enter your HuggingFace token in the sidebar (or set it as a secret).")
else:
    st.info("👆 Upload a PDF to start.")
