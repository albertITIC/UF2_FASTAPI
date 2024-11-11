from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    id: int
    name: str
    classe: str | None = None
    price: float
    tax: float | None = None

# Exemple del tutorial
@app.get("/agenda")
def root():
    return {"1": "albert","2": "alex","3":"victor"}

# GET
@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}

# POST
@app.post("/items/")
async def create_item(item: Item):
    return item