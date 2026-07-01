from datetime import datetime

from sqlmodel import SQLModel, Field


class FacturaBase(SQLModel):
    fecha: datetime = Field(default_factory=datetime.now)


class Factura(FacturaBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

    cliente_id: int = Field(foreign_key="cliente.id")


class FacturaCrear(FacturaBase):
    pass


class FacturaLeer(SQLModel):
    id: int
    fecha: datetime
    cliente_id: int