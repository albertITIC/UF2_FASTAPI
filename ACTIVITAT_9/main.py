from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl # Per poder llegir URL (sense utilitzar str)
from typing import Union # Importar-ho (per fer-ne ús)

# Creo la instància API per manejar rutes i operacions de la API
app = FastAPI()

class Image(BaseModel):
    url: HttpUrl
    name: str
    
# Valida la informació que reb en el cos de la sol·licitud. Podem veure que te els camps de: name, description, price, tax
class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    tags: set[str] = set()
    # Atributs amb llistes de submodels
    images: list[Image] | None = None

# Models profundament anidats
class Offer(BaseModel):
    name: str
    description: str | None = None
    price: float
    items: list[Item]

@app.post("/offers/")
async def create_offer(offer: Offer):
    return offer

# Actualitza un item identificat per item_id
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results