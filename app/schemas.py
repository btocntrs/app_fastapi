from pydantic import BaseModel, Field

class Proveedor(BaseModel):
    id: int | None = None
    rfc: str = Field(..., min_length=12, max_length=13)
    razon_social: str
    nombre_comercial: str | None = None
    productos: str
    banco: str | None = None
    cuenta: str | None = None
    telefono: str | None = None

    class Config:
        orm_mode = True