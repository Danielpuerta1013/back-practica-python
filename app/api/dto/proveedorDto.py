from pydantic import BaseModel,Field
from datetime import date


class ProveedorDTO(BaseModel):
    nombres:str
    documento:str
    direccion:str
    ciudad:str
    representante:str
    telefono:str
    correo:str
    fechaReparto:date
    costoEnvio:int
    descripcion:str
