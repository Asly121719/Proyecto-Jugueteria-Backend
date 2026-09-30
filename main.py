# main.py
import os
import sys

# Permite resolver imports desde la carpeta src
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.database import Base, engine
from src.routers import (
    cargo_router,
    categoria_router,
    cliente_router,
    detalle_venta_router,
    empleado_router,
    garantia_router,
    inventario_router,
    juguete_router,
    promocion_router,
    proveedor_router,
    tienda_router,
    venta_router,
)
from src.seeders import ejecutar_seeders

# Crear las tablas en Neon si no existen
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API Sistema de Gestión de Juguetería",
    version="2.0",
    description="Backend conectado a Neon PostgreSQL con FastAPI, CORS y Swagger completo.",
)

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registrar todos los Routers
app.include_router(categoria_router.router)
app.include_router(cliente_router.router)
app.include_router(juguete_router.router)
app.include_router(tienda_router.router)
app.include_router(empleado_router.router)
app.include_router(cargo_router.router)
app.include_router(proveedor_router.router)
app.include_router(inventario_router.router)
app.include_router(venta_router.router)
app.include_router(detalle_venta_router.router)
app.include_router(promocion_router.router)
app.include_router(garantia_router.router)


@app.on_event("startup")
def startup_event():
    print("Inicializando conexión y seeders con Neon...")
    ejecutar_seeders()


@app.get("/", tags=["Root"])
def read_root():
    return {
        "mensaje": (
            "Bienvenido a la API de la Juguetería v2.0 - Visita /docs para Swagger"
        )
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
