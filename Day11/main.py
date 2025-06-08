from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel


app = FastAPI()


class Item(BaseModel):
    name : str
    price : float
    brand : Optional[str] = None


items = {
    1 : {
        "name" : "Milk",
        "price" : 100,
        "Brand" : "Regular"
    }
}

@app.get("/get-item/{id}")

def get_item(id: int, name:str, test:int):
    return items[id]

@app.get("/get-by-name/{item_id}")

def get_item(*, item_id:int, name:Optional[str]=None):
    for item in items:
        if items[item] ["name"] == name:
            return items[item]
    return "data not  in the items"

@app.post("/create-item")
def create_item(item:Item):
    return {}