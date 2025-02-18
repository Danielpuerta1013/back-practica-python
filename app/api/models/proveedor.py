from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

#llamar a la base de datos

#definir las tablas del api 

class Prooveedor():
    __tablename__ = 'proveedores'
    id= Column(Integer, primary_key=True)
    nombres= Column(String(50))
    documento= Column(String(20))
    direccion= Column(String(50))
    ciudad=Column(String(20))
    representante= Column(String(50))
    telefono= Column(String(20))
    correo= Column(String(50))
    fechaReparto= Column(Date)
    costoEnvio= Column(Integer)
    descripcion= Column(String(200))