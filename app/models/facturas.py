from sqlmodel import SQLModel, Field
from typing import List

class Factura(SQLModel, table=True):

    id: int | None = Field(default=None, primary_key=True)
    fecha: str
    cliente: str
    lista_transacciones: List[float] = []

    def valor_total(self):
        return sum(self.lista_transacciones)