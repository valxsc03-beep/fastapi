from sqlmodel import SQLModel, Field


class TransaccionBase(SQLModel):
    cantidad: int
    valor_unitario: float
    descripcion: str


class Transaccion(TransaccionBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

    factura_id: int = Field(foreign_key="factura.id")


class TransaccionCrear(TransaccionBase):
    pass