from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import proveedores

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Enturamos hacia el modulo de proveedores 
app.include_router(proveedores.router, prefix="/proveedores")