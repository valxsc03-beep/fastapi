from fastapi import APIRouter, HTTPException, status
from sqlmodel import select

from app.database import SessionDependency
from app.models.cliente import Cliente
from app.models.facturas import (
    Factura,
    FacturaCrear,
    FacturaLeerCompuesta,
)

router_facturas = APIRouter()


@router_facturas.get(
    "/facturas",
    response_model=list[FacturaLeerCompuesta]
)
def listar_facturas(session: SessionDependency):
    return session.exec(select(Factura)).all()


@router_facturas.post(
    "/clientes/{cliente_id}/facturas",
    response_model=Factura
)
def crear_factura(
    cliente_id: int,
    datos_factura: FacturaCrear,
    session: SessionDependency
):

    cliente_bd = session.get(Cliente, cliente_id)

    if not cliente_bd:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"El cliente con ID {cliente_id} no existe"
        )

    factura_dict = datos_factura.model_dump()

    factura_dict["cliente_id"] = cliente_id

    factura_nueva = Factura.model_validate(factura_dict)

    session.add(factura_nueva)
    session.commit()
    session.refresh(factura_nueva)

    return factura_nueva