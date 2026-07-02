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


class Factura(FacturaBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    cliente_id: int = Field(foreign_key="cliente.id")

    
    cliente: "Cliente" = Relationship(back_populates="facturas")
    transacciones: list["Transaccion"] = Relationship(back_populates="factura")

    
    @property
    def valor_total(self) -> float:
        if not self.transacciones:
            return 0.0
        return sum(transaccion.monto for transaccion in self.transacciones)


class FacturaCrear(FacturaBase):
    pass

class FacturaEditar(SQLModel):
    descripcion: str | None = None
    monto: float | None = None
    categoria: str | None = None
    estado: str | None = None

class FacturaLeer(SQLModel):
    id: int
    descripcion: str
    monto: float
    categoria: str
    estado: str
    cliente_id: int


class FacturaLeerCompuesta(SQLModel):
    id: int
    descripcion: str
    monto: float
    categoria: str
    estado: str
    cliente_id: int
    
    cliente: ClienteLeer | None = None
    transacciones: list[TransaccionLeer] = []
    
    
    @property
    def valor_total(self) -> float:
        return sum(t.monto for t in self.transacciones) if self.transacciones else 0.0
        
    
    model_config = {"extra": "allow"}