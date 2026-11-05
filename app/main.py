

from fastapi import FastAPI
from openai import OpenAI
from pydantic import BaseModel

app = FastAPI(title="Log Analysis API", 
              description="An API to analyze logs using Qwen2.5:3b model", 
              version="1.0.0")

client = OpenAI(base_url="http://localhost:11434/v1",
                 api_key="ollama")


class LogRequest(BaseModel):
    logs: str

@app.post("/analyze")
def analyze_text(request: LogRequest):
    response = client.chat.completions.create(
        model="qwen2.5:3b",
        messages=[
            {
                "role": "system",
                "content": """
                Eres un ingeniero Senior DevOps especializado en
                Kubernetes, Docker, Linux y aplicaciones .NET.

                Tu tarea es analizar logs técnicos.

                Reglas:
                1. Responde exclusivamente en español.
                2. Identifica primero los errores explícitos del log.
                3. Distingue hechos comprobados de hipótesis.
                4. No inventes información que no aparezca en los logs.
                5. No confundas la construcción de una imagen Docker
                con la ejecución de un contenedor Kubernetes.
                6. Proporciona recomendaciones técnicas verificables.
                7. Si faltan datos para determinar la causa raíz,
                indícalo claramente.

                Estructura de respuesta:
                ERROR DETECTADO:
                EVIDENCIA:
                POSIBLES CAUSAS:
                RECOMENDACIONES:
                """
            },
            {
                "role": "user",
                "content": request.logs
            }
        ],
        temperature=0.2,
    )
    return {"response": response.choices[0].message.content}

