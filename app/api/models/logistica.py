from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base=declarative_base()

class Logistica(Base):
    __tablename__ = 'logistica'
    id= Column(Integer, primary_key=True, autoincrement=True)
    nombreEncargado= Column(String(50))
    correoEncargado= Column(String(100))
    contactoEncargado= Column(String(50))
    fechaRecepcion= Column(Date)
    detalles= Column(String(200))