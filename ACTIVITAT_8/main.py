from fastapi import FastAPI
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
@app.get("/items/{item_id}", status_code=404) # Afegim el status code per si posa un element no 
async def read_item(item_id):
    return {"item_id": item_id}

# POST
@app.post("/items/")
async def create_item(item: Item):
    return item