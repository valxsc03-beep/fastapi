from fastapi import FastAPI

from app.database import crear_bd

from app.routers.cliente import router_cliente
from app.routers.facturas import router_facturas
from app.routers.transacciones import router_transacciones

app = FastAPI()


@app.on_event("startup")
def iniciar_bd():
    crear_bd()


@app.get("/")
def inicio():
    return {"mensaje": "Hola mundo"}


app.include_router(router_cliente)
app.include_router(router_facturas)
app.include_router(router_transacciones)