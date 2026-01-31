from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()

class Question(BaseModel):
    question: str
    style: str

@app.post("/ask")
def ask(data: Question):
    prompt = f"""
You are an AI Study Assistant.
Answer in {data.style} style.

Question:
{data.question}
"""

    headers = {
        "Authorization": "Bearer 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",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "mistralai/mistral-7b-instruct",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    try:
        r = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers=headers,
            json=payload
        )
        answer = r.json()["choices"][0]["message"]["content"]
    except:
        answer = "AI error. Please try again."

    return {"answer": answer}
