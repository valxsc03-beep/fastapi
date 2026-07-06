from datetime import datetime
from typing import TYPE_CHECKING

from sqlmodel import SQLModel, Field, Relationship

from app.models.cliente import ClienteLeer
from app.models.transacciones import TransaccionLeer

if TYPE_CHECKING:
    from app.models.cliente import Cliente
    from app.models.transacciones import Transaccion


class FacturaBase(SQLModel):
    descripcion: str
    monto: float = Field(default=0.0)
    categoria: str
    estado: str = Field(default="pendiente")
    fecha: datetime = Field(default_factory=datetime.now)


class Factura(FacturaBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

    cliente_id: int = Field(foreign_key="cliente.id")

    cliente: "Cliente" = Relationship(back_populates="facturas")

    transacciones: list["Transaccion"] = Relationship(
        back_populates="factura"
    )

    @property
    def valor_total(self) -> float:
        if not self.transacciones:
            return 0.0

        return sum(
            t.cantidad * t.valor_unitario
            for t in self.transacciones
        )


class FacturaCrear(FacturaBase):
    pass


class FacturaEditar(SQLModel):
    descripcion: str | None = None
    monto: float | None = None
    categoria: str | None = None
    estado: str | None = None
    fecha: datetime | None = None


class FacturaLeer(SQLModel):
    id: int
    descripcion: str
    monto: float
    categoria: str
    estado: str
    fecha: datetime
    cliente_id: int


class FacturaLeerCompuesta(SQLModel):
    id: int
    descripcion: str
    monto: float
    categoria: str
    estado: str
    fecha: datetime
    cliente_id: int

    cliente: ClienteLeer | None = None

    transacciones: list[TransaccionLeer] = []

    valor_total: float

    model_config = {"extra": "allow"}