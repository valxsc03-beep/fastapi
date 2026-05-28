from fastapi import APIRouter
from app.models.facturas import Factura

router_facturas = APIRouter()

lista_facturas = []
contador_id = 1

@router_facturas.get("/facturas")
def listar_facturas():
    return {"facturas": lista_facturas}

@router_facturas.post("/facturas")
def crear_factura(datos_factura: Factura):

    global contador_id

    datos_factura.id = contador_id
    contador_id += 1

    lista_facturas.append(datos_factura)

    return {
        "mensaje": "Factura creada",
        "factura": datos_factura
    }

@router_facturas.get("/factura/{factura_id}")
def obtener_factura(factura_id: int):

    for factura in lista_facturas:

        if factura.id == factura_id:
            return factura

    return {"error": "Factura no encontrada"}

@router_facturas.put("/factura/{factura_id}")
def editar_factura(factura_id: int, datos_factura: Factura):

    for i, factura in enumerate(lista_facturas):

        if factura.id == factura_id:

            datos_factura.id = factura_id
            lista_facturas[i] = datos_factura

            return {
                "mensaje": "Factura editada",
                "factura": datos_factura
            }

    return {"error": "Factura no encontrada"}

@router_facturas.delete("/factura/{factura_id}")
def eliminar_factura(factura_id: int):

    for i, factura in enumerate(lista_facturas):

        if factura.id == factura_id:

            factura_eliminada = lista_facturas.pop(i)

            return {
                "mensaje": "Factura eliminada",
                "factura": factura_eliminada
            }

    return {"error": "Factura no encontrada"}