from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base

class Proveedor(Base):
    __tablename__ = "proveedores"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    rfc = Column(String(13), nullable=False, unique=True, index=True)
    razon_social = Column(String(100), nullable=False, unique=True)
    nombre_comercial = Column(String(100), unique=True)
    productos = Column(String(150), nullable=False)
    banco = Column(String(80))
    cuenta = Column(String(50), unique=True)
    telefono = Column(String(20), unique=True)
