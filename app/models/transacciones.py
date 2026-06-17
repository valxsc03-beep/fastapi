from pydantic import BaseModel

class Transaccion(BaseModel):

    id: int = 0
    valor_unitario: float
    cantidad: int
    factura_id: int