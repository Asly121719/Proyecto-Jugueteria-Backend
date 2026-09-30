from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.database import get_db
from src.entities.detalle_venta import DetalleVenta
from src.schemas.detalle_venta_schema import (
    DetalleVentaCreate,
    DetalleVentaResponse,
    DetalleVentaUpdate,
)
from src.utils.constants import (
    HTTP_CREATED,
    HTTP_NO_CONTENT,
    HTTP_NOT_FOUND,
    HTTP_OK,
)

router = APIRouter(prefix="/detalles-venta", tags=["Detalles de Venta"])

@router.get("/", response_model=List[DetalleVentaResponse], status_code=HTTP_OK)
def obtener_detalles(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(DetalleVenta).offset(skip).limit(limit).all()

@router.get("/{id_detalle}", response_model=DetalleVentaResponse, status_code=HTTP_OK)
def obtener_detalle(id_detalle: int, db: Session = Depends(get_db)):
    item = db.query(DetalleVenta).filter(DetalleVenta.id_detalle == id_detalle).first()
    if not item:
        raise HTTPException(status_code=HTTP_NOT_FOUND, detail="Detalle de venta no encontrado")
    return item

@router.post("/", response_model=DetalleVentaResponse, status_code=HTTP_CREATED)
def crear_detalle(data: DetalleVentaCreate, db: Session = Depends(get_db)):
    nuevo = DetalleVenta(**data.dict())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

@router.put("/{id_detalle}", response_model=DetalleVentaResponse, status_code=HTTP_OK)
def actualizar_detalle(id_detalle: int, data: DetalleVentaUpdate, db: Session = Depends(get_db)):
    item = db.query(DetalleVenta).filter(DetalleVenta.id_detalle == id_detalle).first()
    if not item:
        raise HTTPException(status_code=HTTP_NOT_FOUND, detail="Detalle de venta no encontrado")
    for key, value in data.dict(exclude_unset=True).items():
        setattr(item, key, value)
    db.commit()
    db.refresh(item)
    return item

@router.delete("/{id_detalle}", status_code=HTTP_NO_CONTENT)
def eliminar_detalle(id_detalle: int, db: Session = Depends(get_db)):
    item = db.query(DetalleVenta).filter(DetalleVenta.id_detalle == id_detalle).first()
    if not item:
        raise HTTPException(status_code=HTTP_NOT_FOUND, detail="Detalle de venta no encontrado")
    db.delete(item)
    db.commit()
    return None