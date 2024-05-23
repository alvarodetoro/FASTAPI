from pydantic import BaseModel

class Candidato(BaseModel):
    dni: str
    nombre: str
    apellido: str