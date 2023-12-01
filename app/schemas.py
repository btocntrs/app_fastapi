from pydantic import BaseModel

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