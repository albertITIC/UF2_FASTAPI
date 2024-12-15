# Fitxer per controlar els endpoints del joc del penjat amb FastAPI
from fastapi import FastAPI, HTTPException
from typing import List
from pydantic import BaseModel
from conn import *

app = FastAPI()

# Modelo Pydantic per validar la lletra enviada
class NouIntent(BaseModel):
    id_partida: int
    lletra: str

################################################ Punt 0 ################################################
@app.get("/")
async def root():
    return {"Practica 11"}

################################################ Punt 1 ################################################
# Punt per mostrar a tots els usuaris
@app.get("/usuari")
def mostrar_usuaris():
    conn = db_conn()
    cur = conn.cursor()
    
    # Consulta on extreiem tots
    cur.execute("SELECT * FROM USUARI")
    
    # Recollim tots els resultats
    resultat_consulta = cur.fetchall()
    
    # Retornem el resultat
    return resultat_consulta

################################################ Punt 2 ################################################
@app.get("/comencarPartida/button")
def mostrar_text_partida():
    conn = db_conn()
    cur = conn.cursor()
    
    # Consulta on extreiem tots
    cur.execute("SELECT * FROM INFORMACIO")
    
    # Recollim tots els resultats
    resultat_consulta = cur.fetchall()
    
    # Retornem el resultat
    return resultat_consulta

################################################ Punt 3 ################################################
@app.get("/comencarPartida/Text")
def mostrar_text_partida():
    conn = db_conn()
    cur = conn.cursor()
    
    # Consulta on extreiem tots
    cur.execute("SELECT * FROM INFORMACIO")
    
    # Recollim tots els resultats
    resultat_consulta = cur.fetchall()
    
    # Retornem el resultat
    return resultat_consulta


################################################ Punt 4 ################################################
@app.get("/consultar_intents/{id_partida}")
def consultar_intents(id_partida: int):
    conn = db_conn()
    cur = conn.cursor()
    
    try:
        # Consulta els intents restants
        cur.execute("""
            SELECT punts_partides 
            FROM registre_joc 
            WHERE id_partida = %s;
        """, (id_partida,))
        
        resultat = cur.fetchall()  # Obtenim tots els valors de punts_partides
        
        if resultat is None:
            raise HTTPException(status_code=404, detail="Partida no trobada")
        
        # Retorna la id de partida i els intents
        return {
            "id_partida": id_partida,
            "intents_restants": resultat[0]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        conn.close()

# Endpoint POST: Registrar un nou intent
@app.post("/nou_intent/")
def registrar_intent(intent: NouIntent):
    conn = db_conn()
    cur = conn.cursor()

    try:
        # Actualizar el número d'intents i registra la nova lletra
        cur.execute("""
            UPDATE registre_joc 
            SET punts_partides = punts_partides - 1 
            WHERE id_partida = %s
            RETURNING punts_partides
        """, (intent.id_partida,))
        
        resultat = cur.fetchone()
        
        # Important ==> RETURNING punts_partides 
        # retorna el valor actualitzat de punts_partides després de l'operació, UDPATE, de manera automàtica.
        
        
        # Si no troba cap resultat mostrem un error
        if not resultat:
            raise HTTPException(status_code=404, detail="Partida no trobada")
        
        # Retorna el resultat amb la lletra enviada.
        return {
            "missatge": "Intent registrat correctament",    # Missatge per informar que ha sigut afegida
            "lletra": intent.lletra,                        # Mostra la lletra registrada
            "intents_usats": resultat[0]                    # Mostrarà el total d'intents restants
        }
    
    finally:
        conn.commit()
        cur.close()
        conn.close()


################################################ Punt 5 ################################################
@app.get("/alfabet/")
def mostrar_alfabet():
    conn = db_conn()
    cur = conn.cursor()

    try:
        # Consulta para obtener todas las letras del abecedario desde la tabla alfabet
        cur.execute("SELECT lletres FROM alfabet")
        resultats = cur.fetchall()
        
        # If per controlar per si no ha trobat cap lletra
        if not resultats:
            raise HTTPException(status_code=404, detail="No s'ha trobat cap lletra a l'alfabet")

        # Mostrem les lletres
        lletres = [fila[0] for fila in resultats]
        
        # Retornem en format diccionari
        return {
            "alfabet": lletres
        }

    finally:
        cur.close()
        conn.close()
        
################################################ Punt 6 ################################################
# Per fer
@app.get("/consultar_puntuacio/{id_partida}")
def consultar_puntuacio(id_partida: int):
    conn = db_conn()
    cur = conn.cursor()
    
    try:
        # Consulta tots els camps necesaris de la taula 'registre_joc'
        cur.execute("""
            SELECT id_partida, partides_mes_punts, punts_partides, partides_guanyades
            FROM registre_joc 
            WHERE id_partida = %s;
        """, (id_partida,))
        
        resultat = cur.fetchone()  # Obtenim la primera fila de la consulta
        
        if resultat is None:
            raise HTTPException(status_code=404, detail="Partida no trobada")
        
        # Retornem tots els camps
        return {
            "id_partida": resultat[0],            # id_partida
            "partides_mes_punts": resultat[1],    # partides_mes_punts
            "punts_partides": resultat[2],        # punts_partides
            "partides_guanyades": resultat[3]     # partides_guanyades
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        conn.close()
