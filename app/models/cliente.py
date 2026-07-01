from sqlmodel import SQLModel, Field


class ClienteBase(SQLModel):
    nombre: str
    apellido: str
    cedula: str = Field(index=True, unique=True)
    correo: str
    telefono: str


class Cliente(ClienteBase, table=True):
    id: int | None = Field(default=None, primary_key=True)


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