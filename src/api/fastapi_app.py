"""
fastapi_app.py
Small FastAPI app to expose agent endpoints.
"""
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Query(BaseModel):
    q: str

@app.post("/qna")
def qna(query: Query):
    # placeholder response
    return {"answer": "This will be replaced by agent response."}
