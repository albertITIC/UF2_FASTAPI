# Fitxer per controlar els endpoints del joc del penjat amb FastAPI
from fastapi import FastAPI, HTTPException
from typing import List
from pydantic import BaseModel
from conn import *


app = FastAPI()

# Base Model per les taules
# Sol de la puntuació (de moment)
@app.get("/")
async def root():
    return "Hello world"


# Punt de prova
@app.get("/usuari")
def mostrar_usuaris():
    conn = db_conn()
    cur = conn.cursor()
    
    cur.execute("SELECT * FROM USUARI")
    resultat_consulta = cur.fetchall()
    # con.commit -> no cal, insert
    
    return resultat_consulta

# Punt 2    
@app.get("/comencarPartida")
def mostrar_text_partida():
    conn = db_conn()
    cur = conn.cursor()
    
    cur.execute("SELECT * FROM INFORMACIO")
    resultat_consulta = cur.fetchall()
    
    return resultat_consulta