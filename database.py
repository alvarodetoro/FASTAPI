import sqlite3

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

#Para crear la tabla candidato
def create_tables():
    conn = get_db_connection()
    cursor = conn.cursor()
    #DNI será la PRIMARY KEY, porque no deben de haber 2 iguales
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS candidato (
            dni TEXT NOT NULL PRIMARY KEY,
            nombre TEXT NOT NULL,
            apellido TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

#Función para conseguir todos los candidatos de la tabla candidato
def get_all_candidatos():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM candidato")
    candidatos = cursor.fetchall()
    conn.close()
    return candidatos

#Llamar a la función de creación de tabla candidato
create_tables()