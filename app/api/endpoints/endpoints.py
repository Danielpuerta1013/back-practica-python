from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from typing import List
from fastapi.params import Depends

from app.api.dto.proveedorDto import ProveedorDTO
from app.api.dto.proveedorResponse import ProveedorResponse
from app.api.dto.logisticaDto import LogisticaDTO
from app.api.dto.logisticaResponse import logisticaResponse

from app.api.models.logistica import Logistica
from app.api.models.proveedor import Prooveedor


rutas=APIRouter()

#Rutina para conectarnos a la base de datos 
#Rutina para construir servicios web

def guardarProveedor(datosProveedor:ProveedorDTO):
    try:
        Prooveedor(
            nombres=datosProveedor.nombres,
            documento=datosProveedor.documento,
            direccion=datosProveedor.direccion,
            ciudad=datosProveedor.ciudad,
            representante=datosProveedor.representante,
            telefono=datosProveedor.telefono,
            correo=datosProveedor.correo,
            fechaReparto=datosProveedor.fechaReparto,
            costoEnvio=datosProveedor.costoEnvio,
            descripcion=datosProveedor.descripcion,
        )
        
    except Exception as error:
        pass


def guardarLogistica(datosLogistica:LogisticaDTO):
    try:
        Logistica(
            nombreEncargado=datosLogistica.nombreEncargado,
            correoEncargado=datosLogistica.correoEncargado,
            contactoEncargado=datosLogistica.contactoEncargado,
            fechaRecepcion=datosLogistica.fechaRecepcion,
            detalles=datosLogistica.detalles,        
        )
    except Exception as error:
        pass
