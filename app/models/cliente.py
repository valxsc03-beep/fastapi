from typing import TYPE_CHECKING

from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from app.models.facturas import Factura


class ClienteBase(SQLModel):
    nombre: str
    apellido: str
    cedula: str = Field(index=True, unique=True)
    correo: str
    telefono: str


class Cliente(ClienteBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

    facturas: list["Factura"] = Relationship(
        back_populates="cliente"
    )


class ClienteCrear(ClienteBase):
    pass


class ClienteEditar(ClienteBase):
    pass


class ClienteLeer(SQLModel):
    id: int
    nombre: str
    apellido: str
    cedula: str
    correo: str
    telefono: str