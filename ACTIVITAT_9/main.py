from typing import Annotated

from fastapi import Body, FastAPI
from pydantic import BaseModel, Field

# Creo la instància API per manejar rutes i operacions de la API
app = FastAPI()

# Valida la informació que reb en el cos de la sol·licitud. Podem veure que te els camps de: name, description, price, tax
class Item(BaseModel):
    name: str
    description: str | None = Field(
        default=None, title="The description of the item", max_length=300
    )
    price: float = Field(gt=0, description="The price must be greater than zero")
    tax: float | None = None

# Actualitza un item identificat per item_id
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Annotated[Item, Body(embed=True)]):
    results = {"item_id": item_id, "item": item}
    return results