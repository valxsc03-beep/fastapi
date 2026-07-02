from fastapi import APIRouter, HTTPException, status
from sqlmodel import select
from app.database import SessionDependency
from app.models.facturas import (
    Factura, 
    FacturaCrear, 
    FacturaEditar, 
    FacturaLeer, 
    FacturaLeerCompuesta
)
from app.models.cliente import Cliente


router_facturas = APIRouter(tags=["Facturas"])


@router_facturas.get("/facturas", response_model=list[FacturaLeerCompuesta])
def listar_facturas(session: SessionDependency):
    return session.exec(select(Factura)).all()



@router_facturas.get("/facturas/{factura_id}", response_model=FacturaLeerCompuesta)
def obtener_factura(factura_id: int, session: SessionDependency):
    factura_bd = session.get(Factura, factura_id)
    if not factura_bd:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"La factura con ID {factura_id} no existe."
        )
    return factura_bd



@router_facturas.post("/clientes/{cliente_id}/facturas", response_model=FacturaLeer, status_code=status.HTTP_201_CREATED)
def crear_factura(cliente_id: int, datos_factura: FacturaCrear, session: SessionDependency):
    cliente_bd = session.get(Cliente, cliente_id)
    if not cliente_bd:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"El cliente con ID {cliente_id} no existe."
        )
    
    factura_dict = datos_factura.model_dump()
    factura_dict["cliente_id"] = cliente_id
    
    factura_nueva = Factura.model_validate(factura_dict)
    
    session.add(factura_nueva)
    session.commit()
    session.refresh(factura_nueva)
    
    return factura_nueva


@router_facturas.patch("/facturas/{factura_id}", response_model=FacturaLeer)
def editar_factura(factura_id: int, datos_factura: FacturaEditar, session: SessionDependency):
    factura_bd = session.get(Factura, factura_id)
    if not factura_bd:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"La factura con ID {factura_id} no existe para modificar."
        )
        
    factura_dict = datos_factura.model_dump(exclude_unset=True)
    factura_bd.sqlmodel_update(factura_dict)
    
    session.add(factura_bd)
    session.commit()
    session.refresh(factura_bd)
    
    return factura_bd


@router_facturas.delete("/facturas/{factura_id}")
def eliminar_factura(factura_id: int, session: SessionDependency):
    factura_bd = session.get(Factura, factura_id)
    if not factura_bd:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"La factura con ID {factura_id} no existe para eliminar."
        )
        
    session.delete(factura_bd)
    session.commit()
    
    return {"mensaje": f"La factura con ID {factura_id} fue eliminada exitosamente."}