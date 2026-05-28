from fastapi import APIRouter
from app.models.transacciones import Transaccion

router_transacciones = APIRouter()

lista_transacciones = []
contador_id = 1

@router_transacciones.get("/transacciones")
def listar_transacciones():
    return {"transacciones": lista_transacciones}

@router_transacciones.post("/transacciones")
def crear_transaccion(datos_transaccion: Transaccion):

    global contador_id

    datos_transaccion.id = contador_id
    contador_id += 1

    lista_transacciones.append(datos_transaccion)

    return {
        "mensaje": "Transacción creada",
        "transaccion": datos_transaccion
    }

@router_transacciones.get("/transaccion/{transaccion_id}")
def obtener_transaccion(transaccion_id: int):

    for transaccion in lista_transacciones:

        if transaccion.id == transaccion_id:
            return transaccion

    return {"error": "Transacción no encontrada"}

@router_transacciones.put("/transaccion/{transaccion_id}")
def editar_transaccion(transaccion_id: int, datos_transaccion: Transaccion):

    for i, transaccion in enumerate(lista_transacciones):

        if transaccion.id == transaccion_id:

            datos_transaccion.id = transaccion_id
            lista_transacciones[i] = datos_transaccion

            return {
                "mensaje": "Transacción editada",
                "transaccion": datos_transaccion
            }

    return {"error": "Transacción no encontrada"}

@router_transacciones.delete("/transaccion/{transaccion_id}")
def eliminar_transaccion(transaccion_id: int):

    for i, transaccion in enumerate(lista_transacciones):

        if transaccion.id == transaccion_id:

            transaccion_eliminada = lista_transacciones.pop(i)

            return {
                "mensaje": "Transacción eliminada",
                "transaccion": transaccion_eliminada
            }

    return {"error": "Transacción no encontrada"}