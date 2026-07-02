from typing import TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship


if TYPE_CHECKING:
    from app.models.facturas import Factura


class TransaccionBase(SQLModel):
    descripcion: str
    cantidad: int = Field(default=0)
    valor_unitario: float = Field(default=0.0)


class Transaccion(TransaccionBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    factura_id: int = Field(foreign_key="factura.id")

   
    factura: "Factura" = Relationship(back_populates="transacciones")


class TransaccionCrear(TransaccionBase):
    pass


class TransaccionEditar(TransaccionBase):
    pass


class TransaccionLeer(SQLModel):
    id: int
    descripcion: str
    cantidad: int
    valor_unitario: float
    factura_id: int

class TransaccionLeerCompuesta(TransaccionLeer):
    pass