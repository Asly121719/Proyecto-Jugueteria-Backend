# src/routers/venta_router.py
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.database import get_db
from src.entities.venta import Venta
from src.schemas.venta_schema import VentaCreate, VentaResponse, VentaUpdate
from src.utils.constants import (
    HTTP_CREATED,
    HTTP_NO_CONTENT,
    HTTP_NOT_FOUND,
    HTTP_OK,
)

router = APIRouter(prefix="/ventas", tags=["Ventas"])

@router.get("/", response_model=List[VentaResponse], status_code=HTTP_OK)
def obtener_ventas(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(Venta).offset(skip).limit(limit).all()

@router.get("/{id_venta}", response_model=VentaResponse, status_code=HTTP_OK)
def obtener_venta(id_venta: int, db: Session = Depends(get_db)):
    item = db.query(Venta).filter(Venta.id_venta == id_venta).first()
    if not item:
        raise HTTPException(status_code=HTTP_NOT_FOUND, detail="Venta no encontrada")
    return item

@router.post("/", response_model=VentaResponse, status_code=HTTP_CREATED)
def crear_venta(data: VentaCreate, db: Session = Depends(get_db)):
    nuevo = Venta(**data.dict())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

@router.put("/{id_venta}", response_model=VentaResponse, status_code=HTTP_OK)
def actualizar_venta(id_venta: int, data: VentaUpdate, db: Session = Depends(get_db)):
    item = db.query(Venta).filter(Venta.id_venta == id_venta).first()
    if not item:
        raise HTTPException(status_code=HTTP_NOT_FOUND, detail="Venta no encontrada")
    for key, value in data.dict(exclude_unset=True).items():
        setattr(item, key, value)
    db.commit()
    db.refresh(item)
    return item

@router.delete("/{id_venta}", status_code=HTTP_NO_CONTENT)
def eliminar_venta(id_venta: int, db: Session = Depends(get_db)):
    item = db.query(Venta).filter(Venta.id_venta == id_venta).first()
    if not item:
        raise HTTPException(status_code=HTTP_NOT_FOUND, detail="Venta no encontrada")
    db.delete(item)
    db.commit()
    return None