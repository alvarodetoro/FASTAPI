from fastapi import FastAPI, HTTPException
import sqlite3
from database import get_db_connection, get_all_candidatos
from models import Candidato


app = FastAPI()
#Página principal
@app.get("/")
def index():
    return{"message":""}

#Método para seleccionar todos los candidatos en la base de datos
@app.get("/candidatos")
def get_candidatos():
    #Llamada a la funcion de database.py para llamar a todos los candidatos
    candidatos = get_all_candidatos()
    #En caso de no encontrar ningún candidato en la base de datos salta el error
    if not candidatos:
        raise HTTPException(status_code=404, detail="No se encontraron candidatos")
    return candidatos

#Método para insertar un nuevo candidato en la base de datos
@app.post("/candidato")
def crear_candidato(candidato: Candidato):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(''' INSERT INTO candidato (dni, nombre, apellido) VALUES (?,?,?)''', (candidato.dni, candidato.nombre, candidato.apellido))
        conn.commit()
    except sqlite3.IntegrityError as e:
        raise HTTPException(status_code=400, detail="El candidato ya existe")
    finally:
        conn.close()

#Método para borrar un candidato de la base de datos en base al DNI
@app.delete("/candidato/{dni}")
def delete_candidato(dni: str):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM candidato WHERE dni = ?", (dni,))
    #Si no encuentra el DNI de la persona, salta error
    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="El candidato no se encontrado")
    conn.commit()
    conn.close()
    return {"message": f"El candidato con DNI {dni} eliminado exitosamente"}
