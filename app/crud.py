from sqlalchemy.orm import Session

from . import models, schemas

# Metodo para los proveedores
def get_proveedor_by_rfc(db: Session, rfc: str):
    return db.query(models.Proveedor).filter(models.Proveedor.rfc == rfc).first()

def get_proveedores(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Proveedor).offset(skip).limit(limit).all()

def create_proveedor(db: Session, proveedor: schemas.Proveedor):
    db_proveedor = models.Proveedor(rfc = proveedor.rfc, 
                                    razon_social = proveedor.razon_social,
                                    nombre_comercial = proveedor.nombre_comercial,
                                    productos = proveedor.productos,
                                    banco = proveedor.banco,
                                    cuenta = proveedor.cuenta,
                                    telefono = proveedor.telefono)
    db.add(db_proveedor)
    db.commit()
    db.refresh(db_proveedor)
    return db_proveedor

def update_proveedor(db: Session, rfc: str, updated_proveedor: schemas.Proveedor):
    # Obtén el proveedor existente por su RFC
    db_proveedor = get_proveedor_by_rfc(db, rfc)

    if db_proveedor is None:
        return None  # Opcional: Puedes manejar el caso de que el proveedor no exista

    # Actualiza los atributos del proveedor con los nuevos valores
    for attr, value in updated_proveedor:
        setattr(db_proveedor, attr, value)

    db.commit()
    db.refresh(db_proveedor)
    return db_proveedor

def delete_proveedor(db: Session, rfc: str, updated_proveedor: schemas.Proveedor):
    # Obtén el proveedor existente por su RFC
    db_proveedor = get_proveedor_by_rfc(db, rfc)

    if db_proveedor is None:
        return None  # Opcional: Puedes manejar el caso de que el proveedor no exista

    db.delete(db_proveedor)
    db.commit()
    return db_proveedor

def delete_proveedor(db: Session, rfc: str):
    # Obtén el proveedor existente por su RFC
    db_proveedor = get_proveedor_by_rfc(db, rfc)

    if db_proveedor is None:
        return None  # Opcional: Puedes manejar el caso de que el proveedor no exista

    db.delete(db_proveedor)
    db.commit()
    return db_proveedor