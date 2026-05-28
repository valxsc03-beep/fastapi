from pydantic import BaseModel
from typing import List

class Factura(BaseModel):

    id: int = 0
    fecha: str
    cliente: str
    lista_transacciones: List[float] = []

    def valor_total(self):
        return sum(self.lista_transacciones)