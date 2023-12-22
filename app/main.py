from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Este método obtiene la lista de proveedores completa
@app.get("/proveedores/", response_model=list[schemas.Proveedor], status_code=status.HTTP_200_OK)
def read_proveedores(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    proveedores = crud.get_proveedores(db, skip=skip, limit=limit)
    return proveedores

@app.get("/proveedores/{rfc_proveedor}", response_model=schemas.Proveedor, status_code=status.HTTP_200_OK)
def read_proveedor_by_rfc(rfc_proveedor: str, db: Session = Depends(get_db)):
    db_proveedor = crud.get_proveedor_by_rfc(db, rfc=rfc_proveedor)
    if db_proveedor is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Proveedor no encontrado")
    return db_proveedor

@app.post("/proveedores/", response_model=schemas.Proveedor, status_code=status.HTTP_201_CREATED)
def create_proveedor(proveedor: schemas.Proveedor, db: Session = Depends(get_db)):
    db_proveedor = crud.get_proveedor_by_rfc(db, rfc=proveedor.rfc)
    if db_proveedor:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Proveedor ya registrado")
    return crud.create_proveedor(db=db, proveedor=proveedor)

@app.put("/proveedores/", response_model=schemas.Proveedor, status_code=status.HTTP_200_OK)
def update_proveedor(updated_proveedor: schemas.Proveedor, db: Session = Depends(get_db)):
    db_proveedor = crud.get_proveedor_by_rfc(db, rfc=updated_proveedor.rfc)
    
    if db_proveedor is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Proveedor no encontrado")
    else:
        db_proveedor = crud.update_proveedor(db, updated_proveedor.rfc, updated_proveedor)

    return db_proveedor

@app.put("/proveedores/{rfc}", response_model=schemas.Proveedor, status_code=status.HTTP_200_OK)
def update_proveedor(rfc: str, updated_proveedor: schemas.Proveedor, db: Session = Depends(get_db)):
    db_proveedor = crud.get_proveedor_by_rfc(db, rfc=updated_proveedor.rfc)
    
    if db_proveedor is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Proveedor no encontrado")
    else:
        db_proveedor = crud.update_proveedor(db, rfc, updated_proveedor)

    return db_proveedor

@app.delete("/proveedores/", response_model=schemas.Proveedor, status_code=status.HTTP_200_OK)
def delete_proveedor(proveedor: schemas.Proveedor, db: Session = Depends(get_db)):
    deleted_proveedor = crud.delete_proveedor(db, proveedor.rfc)
    if deleted_proveedor:
        return deleted_proveedor
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Proveedor no encontrado")

@app.delete("/proveedores/{rfc}", status_code=status.HTTP_200_OK)
def delete_proveedor(rfc: str, db: Session = Depends(get_db)):
    deleted_proveedor = crud.delete_proveedor(db, rfc)
    if deleted_proveedor:
        return deleted_proveedor
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Proveedor no encontrado")