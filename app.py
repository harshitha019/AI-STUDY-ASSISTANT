import streamlit as st
import requests

BACKEND = "http://127.0.0.1:8000"

st.set_page_config(page_title="AI Study Assistant")
st.title("📘 AI Study Assistant")

style = st.selectbox(
    "Answer style",
    ["Simple", "Detailed", "Exam-ready"]
)

question = st.text_input("Ask your study question")

if st.button("Ask"):
    if question:
        r = requests.post(
            f"{BACKEND}/ask",
            json={
                "question": question,
                "style": style
            }
        )

        if r.status_code == 200:
            st.write(r.json()["answer"])
        else:
            st.error("Backend error")
