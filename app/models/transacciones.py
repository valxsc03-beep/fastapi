from sqlmodel import SQLModel, Field


class TransaccionBase(SQLModel):
    descripcion: str
    cantidad: int = Field(default=0)
    valor_unitario: float = Field(default=0.0)


class Transaccion(TransaccionBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

    factura_id: int = Field(foreign_key="factura.id")


class TransaccionCrear(TransaccionBase):
    pass


class TransaccionLeer(SQLModel):
    id: int
    descripcion: str
    cantidad: int
    valor_unitario: float
    factura_id: int