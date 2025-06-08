from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

@app.get('/blog')
def index(limit: int = 10, published: bool = True, sort: Optional[str] = None):
    if published:
        return {'data': f'{limit} published blogs from the db'}
    else:
        return {'data': f'{limit} blogs from the db'}

@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'all unpublished blogs'}

@app.get('/blog/{id}/comments')
def comments(id: int, limit: int = 10):
    return {'data': ['comment 1', 'comment 2']}

class Blog(BaseModel):
    title : str
    body : str
    published : Optional[bool]

@app.post('/blog')

def create_blog(request:Blog):
    
    return {'data':f"Blogs is created with title as {request.title}"} 