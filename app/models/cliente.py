from sqlmodel import SQLModel, Field

class Cliente(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    nombre: str
    edad: int
    descripcion: str