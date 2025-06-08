from fastapi import FastAPI

app = FastAPI()



@app.get('/')

def root():
    return {'data':'blog list'}

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