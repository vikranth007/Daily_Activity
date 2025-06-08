from fastapi import FastAPI
import uvicorn




app = FastAPI()


@app.get('/blog')
def predict():
    return "Welcome"


@app.post('/predict')
def pred():
    return hi



if __name__ == "__main__":
    uvicorn = 