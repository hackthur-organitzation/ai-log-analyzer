from fastapi import FastAPI
from openai import OpenAI


app = FastAPI()

@app.get("/")
def read_root():
    return {"Mesage":"Hello hackthur"}


def main():
    client = OpenAI()
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Hello! How can I use the OpenAI API in my FastAPI application?"}
        ]
    )
    print(response.choices[0].message.content)