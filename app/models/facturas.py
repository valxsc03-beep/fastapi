from datetime import datetime
from typing import TYPE_CHECKING

from sqlmodel import SQLModel, Field, Relationship

from app.models.cliente import ClienteLeer
from app.models.transacciones import TransaccionLeer

if TYPE_CHECKING:
    from app.models.cliente import Cliente
    from app.models.transacciones import Transaccion


class FacturaBase(SQLModel):
    fecha: datetime = Field(default_factory=datetime.now)


class Factura(FacturaBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

    cliente_id: int = Field(foreign_key="cliente.id")

    cliente: "Cliente" = Relationship(
        back_populates="facturas"
    )

    transacciones: list["Transaccion"] = Relationship(
        back_populates="factura"
    )

    @property
    def valor_total(self) -> float:
        if not self.transacciones:
            return 0.0

        total = 0.0

        for transaccion in self.transacciones:
            total += (
                transaccion.cantidad
                * transaccion.valor_unitario
            )

        return total


class FacturaCrear(FacturaBase):
    pass


class FacturaLeer(SQLModel):
    id: int
    fecha: datetime
    cliente_id: int


class FacturaLeerCompuesta(SQLModel):
    id: int
    fecha: datetime
    cliente_id: int

    cliente: ClienteLeer

    transacciones: list[TransaccionLeer] = []

    valor_total: float