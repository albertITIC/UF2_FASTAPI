from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Crear una instància Fastapi
app = FastAPI()

# Creació d'un model de dades amb nom "Item"
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
    # Retornem un diccionari
    return {"1": "albert","2": "alex","3":"victor"}

# GET (id amb status d'error)
# Endpoint que agafa l'id i llença un error mitjançant l'status code 404
@app.get("/items/{item_id}", status_code=404) # Afegim el status code per si posa un element no 
async def read_item(item_id):
    return {"item_id": item_id}

# Diccionari d'exemple
items = {"foo": "The Foo Wrestlers"}

# Endpoint que li passem per paràmetre una id
@app.get("/items/{item_id}")
async def read_item(item_id: str):
    # Verifiquem que l'item es trobi dins del diccionari
    if item_id not in items:
        # Si no el troba, llença l'exepció d'error 404 amb el nostre missatge personalitzat
        raise HTTPException(status_code=404, detail="Ítem no trobat, siusplau introdueix una id existent")
    # Si exiteix el retorarà
    return {"item": items[item_id]}

# POST
@app.post("/items/")
# Reb un item verificant els camps, aquests han d'estar correctes per retronar-los
async def create_item(item: Item):
    return item