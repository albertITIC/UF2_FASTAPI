# Fitxer per controlar els endpoints del joc del penjat amb FastAPI
from fastapi import FastAPI, HTTPException
from typing import List
from pydantic import BaseModel

app = FastAPI

# Base Model per les taules
# Sol de la puntuació (de moment)

# Punt 2
@app.get("/")
def missatge():
    return {
        "Missatge" : "Començar partida" 
            }
    
# Punt 3
@app.get("/")
def missatge():
    return {
        "Missatge" : "Començar partida" 
            }
    
    
    