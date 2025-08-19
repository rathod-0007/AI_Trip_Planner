from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class QueryRequest(BaseModel):
    query: str

@app.post("/query")
async def query_api(request: QueryRequest):
    return {"response": f"You asked: {request.query}"}
