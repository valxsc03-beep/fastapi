from fastapi import APIRouter, HTTPException, status
from sqlmodel import select

from app.database import SessionDependency
from app.models.facturas import Factura
from app.models.transacciones import (
    Transaccion,
    TransaccionCrear,
)

router_transacciones = APIRouter()


@router_transacciones.get("/transacciones", response_model=list[Transaccion])
def listar_transacciones(session: SessionDependency):
    return session.exec(select(Transaccion)).all()


@router_transacciones.post(
    "/facturas/{factura_id}/transacciones",
    response_model=Transaccion
)
def crear_transaccion(
    factura_id: int,
    datos_transaccion: TransaccionCrear,
    session: SessionDependency
):
   
    factura_bd = session.get(Factura, factura_id)

    if not factura_bd:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"La factura con ID {factura_id} no existe"
        )

    
    transaccion_dict = datos_transaccion.model_dump()

    
    transaccion_dict["factura_id"] = factura_id

    
    nueva_transaccion = Transaccion.model_validate(transaccion_dict)

    
    session.add(nueva_transaccion)
    session.commit()
    session.refresh(nueva_transaccion)

    return nueva_transaccion