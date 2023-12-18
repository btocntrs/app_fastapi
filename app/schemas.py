from pydantic import BaseModel

#Este clase crea una tabla en la base da datos si hace falta junto con la estructura de los datos
class Proveedor(BaseModel):
    id: int | None = None
    rfc: str
    razon_social: str
    nombre_comercial: str | None = None
    productos: str
    banco: str | None = None
    cuenta: str | None = None
    telefono: str | None = None

    class Config:
        orm_mode = True