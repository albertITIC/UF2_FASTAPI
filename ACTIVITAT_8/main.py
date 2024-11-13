from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI()

class Item(BaseModel):
    numLlista: int
    name: str
    classe: str
    altura: int
    pes: int | None = None # Opcional
    sexe: str

# Exemple diccionari - exercici 1 
@app.get("/agenda")
def root():
    return {"1": "albert","2": "alex","3":"victor"}

# GET (id amb status d'error)
# @app.get("/items/{item_id}", status_code=404) # Afegim el status code per si posa un element no 
# async def read_item(item_id):
#     return {"item_id": item_id}

items = {"foo": "The Foo Wrestlers"}
@app.get("/items/{item_id}")
async def read_item(item_id: str):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Ítem no trobat, siusplau introdueix una id existent")
    return {"item": items[item_id]}

# POST
@app.post("/items/")
async def create_item(item: Item):
    return item