from fastapi import FastAPI
from enum import Enum



app = FastAPI()


class Availablecusine(str, Enum):
    indian = 'indian'
    american = 'american'
    italian = 'italian'

food_items = {
    'indian' : ['Samosa', 'Dosa'],
    'american' : ['Hot', 'apple_pie'],
    'italian' : ['Ravioli', 'pizza']
}

valid_cusine = food_items.keys()


@app.get("/get_items/{cuisine}")
async def get_items(cuisine:Availablecusine):
    return food_items.get(cuisine)