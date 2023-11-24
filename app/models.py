from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base

class Proveedor(Base):
    __tablename__ = "proveedores"
    
    rfc = Column(String, primary_key=True, index=True)
    razon_social = Column(String, nullable=False, unique=True)
    nombre_comercial = Column(String, unique=True)
    productos = Column(String, nullable=False)
    banco = Column(String)
    cuenta = Column(String, unique=True)
    telefono = Column(String, unique=True)
