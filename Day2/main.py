from fastapi import FastAPI
from typing import Optional

app = FastAPI()



@app.get('/blog')

def root(limit=10, published:bool=True,sort:Optional[str]=None):
    

    
    if published:
        return {'data': f'{limit} published blog from the database'}
    else:
        return {'data': f'{limit}  blog from the database'}


@app.get('blog/inpublished')
def unpublised():
    return {'data':'unpublished blogs'}

@app.get('/blog/{id}')

def show(id:int):
    # fetch blog with id = id
    return {'data':id}



@app.get('/blog/{id}/comments')

def comments(id):
    return {'data': {'1', '2', '3'}}