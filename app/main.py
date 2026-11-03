

from fastapi import FastAPI
from openai import OpenAI
from pydantic import BaseModel

app = FastAPI(title="Log Analysis API", description="An API to analyze logs using Qwen2.5:3b model", version="1.0.0")

client = OpenAI(base_url="http://localhost:11434/v1",
                 api_key="ollama")


class LogRequest(BaseModel):
    logs: str

@app.get("/")
def read_root():
    return {"Message":"Hello hackthur"}

# define a post endpoint to analyze the log using qwen2.5:3b

@app.post("/analyze")
def analyze_text(request: LogRequest):
    response = client.chat.completions.create(
        model="qwen2.5:3b",
        messages=[
            {
                "role": "system",
                "content": (
                    "Eres un ingeniero DevOps especializado en "
                    "Kubernetes, Linux y troubleshooting. "
                    "Analiza los logs proporcionados. "
                    "Responde exclusivamente en español. "
                    "Identifica errores, posibles causas y "
                    "recomendaciones. No inventes evidencias."
                )
            },
            {
                "role": "user",
                "content": request.logs
            }
        ],
        temperature=0.2,
    )
    return {"response": response.choices[0].message.content}

