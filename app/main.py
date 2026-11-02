from fastapi import FastAPI
from openai import OpenAI


app = FastAPI()

@app.get("/")
def read_root():
    return {"Mesage":"Hello hackthur"}


