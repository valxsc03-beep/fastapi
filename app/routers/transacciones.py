from fastapi import APIRouter, HTTPException, status
from sqlmodel import select
from app.database import SessionDependency
from app.models.transacciones import (
    Transaccion, 
    TransaccionCrear, 
    TransaccionEditar, 
    TransaccionLeer
)
from app.models.facturas import Factura


router_transacciones = APIRouter(tags=["Transacciones"])

@router_transacciones.get("/transacciones", response_model=list[TransaccionLeer])
def listar_transacciones(session: SessionDependency):
    return session.exec(select(Transaccion)).all()


@router_transacciones.get("/transacciones/{transaccion_id}", response_model=TransaccionLeer)
def obtener_transaccion(transaccion_id: int, session: SessionDependency):
    transaccion_bd = session.get(Transaccion, transaccion_id)
    if not transaccion_bd:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"La transacción con ID {transaccion_id} no existe."
        )
    return transaccion_bd


@router_transacciones.post("/facturas/{factura_id}/transacciones", response_model=TransaccionLeer, status_code=status.HTTP_201_CREATED)
def crear_transaccion(factura_id: int, datos_transaccion: TransaccionCrear, session: SessionDependency):
    factura_bd = session.get(Factura, factura_id)
    if not factura_bd:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"La factura con ID {factura_id} no existe."
        )
    
    transaccion_dict = datos_transaccion.model_dump()
    transaccion_dict["factura_id"] = factura_id
    
    transaccion_nueva = Transaccion.model_validate(transaccion_dict)
    
    session.add(transaccion_nueva)
    session.commit()
    session.refresh(transaccion_nueva)
    return transaccion_nueva


@router_transacciones.patch("/transacciones/{transaccion_id}", response_model=TransaccionLeer)
def editar_transaccion(transaccion_id: int, datos_transaccion: TransaccionEditar, session: SessionDependency):
    transaccion_bd = session.get(Transaccion, transaccion_id)
    if not transaccion_bd:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"La transacción con ID {transaccion_id} no existe para modificar."
        )
    
    transaccion_dict = datos_transaccion.model_dump(exclude_unset=True)
    transaccion_bd.sqlmodel_update(transaccion_dict)
    
    session.add(transaccion_bd)
    session.commit()
    session.refresh(transaccion_bd)
    return transaccion_bd


@router_transacciones.delete("/transacciones/{transaccion_id}")
def eliminar_transaccion(transaccion_id: int, session: SessionDependency):
    transaccion_bd = session.get(Transaccion, transaccion_id)
    if not transaccion_bd:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"La transacción con ID {transaccion_id} no existe para eliminar."
        )
    
    session.delete(transaccion_bd)
    session.commit()
    return {"mensaje": f"La transacción con ID {transaccion_id} fue eliminada exitosamente."}