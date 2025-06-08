from fastapi import FastAPI
from pydantic import BaseModel




app = FastAPI()

class Blog(BaseModel):
    title : str
    body : str


@app.post('/blog')
def create_model(request:Blog):
    return request