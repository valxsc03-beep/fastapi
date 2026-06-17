from sqlmodel import SQLModel, Field

class Factura(SQLModel, table=True):

    id: int | None = Field(default=None, primary_key=True)
    fecha: str
    cliente: str

    def valor_total(self):
        return 0