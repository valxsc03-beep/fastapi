from fastapi import APIRouter, HTTPException, status
from sqlmodel import select

from app.database import SessionDependency
from app.models.cliente import (
    Cliente,
    ClienteCrear,
    ClienteEditar,
)

router_cliente = APIRouter()


@router_cliente.get("/clientes", response_model=list[Cliente])
def listar_clientes(session: SessionDependency):
    return session.exec(select(Cliente)).all()


@router_cliente.post("/clientes", response_model=Cliente)
def crear_cliente(datos_cliente: ClienteCrear, session: SessionDependency):

    cliente_nuevo = Cliente.model_validate(datos_cliente)

    session.add(cliente_nuevo)
    session.commit()
    session.refresh(cliente_nuevo)

    return cliente_nuevo


@router_cliente.get("/clientes/{cliente_id}", response_model=Cliente)
def obtener_cliente(cliente_id: int, session: SessionDependency):

    cliente_bd = session.get(Cliente, cliente_id)

    if not cliente_bd:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"El cliente con ID {cliente_id} no existe"
        )

    return cliente_bd


@router_cliente.patch("/clientes/{cliente_id}", response_model=Cliente)
def editar_cliente(
    cliente_id: int,
    datos_cliente: ClienteEditar,
    session: SessionDependency
):

    cliente_bd = session.get(Cliente, cliente_id)

    if not cliente_bd:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Cliente no encontrado"
        )

    cliente_dict = datos_cliente.model_dump(exclude_unset=True)

    cliente_bd.sqlmodel_update(cliente_dict)

    session.add(cliente_bd)
    session.commit()
    session.refresh(cliente_bd)

    return cliente_bd


@router_cliente.delete("/clientes/{cliente_id}")
def eliminar_cliente(
    cliente_id: int,
    session: SessionDependency
):

    cliente_bd = session.get(Cliente, cliente_id)

    if not cliente_bd:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Cliente no encontrado"
        )

    session.delete(cliente_bd)
    session.commit()

    return {
        "mensaje": f"El cliente con ID {cliente_id} fue eliminado exitosamente"
    }