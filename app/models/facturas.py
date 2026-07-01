from datetime import datetime

from sqlmodel import SQLModel, Field


class FacturaBase(SQLModel):
    fecha: datetime = Field(default_factory=datetime.now)


class Factura(FacturaBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

    cliente_id: int = Field(foreign_key="cliente.id")

    @property
    def valor_total(self):
        return 0.0


class FacturaCrear(FacturaBase):
    pass