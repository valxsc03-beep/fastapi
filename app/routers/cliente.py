from fastapi import APIRouter
from app.models.cliente import Cliente

router_cliente = APIRouter()

lista_clientes = []
contador_id = 1

@router_cliente.get("/clientes")
def listar_clientes():
    return {"clientes": lista_clientes}

@router_cliente.post("/clientes")
def crear_clientes(datos_cliente: Cliente):
    global contador_id

    datos_cliente.id = contador_id
    contador_id += 1

    lista_clientes.append(datos_cliente)

    return {
        "mensaje": "Cliente creado",
        "cliente": datos_cliente
    }

@router_cliente.get("/cliente/{cliente_id}")
def obtener_cliente(cliente_id: int):
    for cliente in lista_clientes:
        if cliente.id == cliente_id:
            return cliente
    return {"error": "Cliente no encontrado"}

@router_cliente.put("/cliente/{cliente_id}")
def editar_cliente(cliente_id: int, datos_clientes: Cliente):
    for i, cliente in enumerate(lista_clientes):
        if cliente.id == cliente_id:
            datos_clientes.id = cliente_id
            lista_clientes[i] = datos_clientes
            return {
                "mensaje": "Cliente editado",
                "cliente": datos_clientes
            }
    return {"error": "Cliente no encontrado"}

@router_cliente.delete("/cliente/{cliente_id}")
def eliminar_cliente(cliente_id: int):
    for i, cliente in enumerate(lista_clientes):
        if cliente.id == cliente_id:
            cliente_eliminado = lista_clientes.pop(i)
            return {
                "mensaje": "Cliente eliminado",
                "cliente": cliente_eliminado
            }
    return {"error": "Cliente no encontrado"}