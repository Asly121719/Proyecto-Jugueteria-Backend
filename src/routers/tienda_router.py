from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.database import get_db
from src.entities.Tienda import Tienda
from src.schemas.tienda_schema import TiendaCreate, TiendaResponse, TiendaUpdate
from src.utils.constants import (
    HTTP_CREATED,
    HTTP_NO_CONTENT,
    HTTP_NOT_FOUND,
    HTTP_OK,
)

router = APIRouter(prefix="/tiendas", tags=["Tiendas"])

@router.get("/", response_model=List[TiendaResponse], status_code=HTTP_OK)
def obtener_tiendas(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(Tienda).offset(skip).limit(limit).all()

@router.get("/{id_tienda}", response_model=TiendaResponse, status_code=HTTP_OK)
def obtener_tienda(id_tienda: int, db: Session = Depends(get_db)):
    item = db.query(Tienda).filter(Tienda.id_tienda == id_tienda).first()
    if not item:
        raise HTTPException(status_code=HTTP_NOT_FOUND, detail="Tienda no encontrada")
    return item

@router.post("/", response_model=TiendaResponse, status_code=HTTP_CREATED)
def crear_tienda(data: TiendaCreate, db: Session = Depends(get_db)):
    nuevo = Tienda(**data.dict())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

@router.put("/{id_tienda}", response_model=TiendaResponse, status_code=HTTP_OK)
def actualizar_tienda(id_tienda: int, data: TiendaUpdate, db: Session = Depends(get_db)):
    item = db.query(Tienda).filter(Tienda.id_tienda == id_tienda).first()
    if not item:
        raise HTTPException(status_code=HTTP_NOT_FOUND, detail="Tienda no encontrada")
    for key, value in data.dict(exclude_unset=True).items():
        setattr(item, key, value)
    db.commit()
    db.refresh(item)
    return item

@router.delete("/{id_tienda}", status_code=HTTP_NO_CONTENT)
def eliminar_tienda(id_tienda: int, db: Session = Depends(get_db)):
    item = db.query(Tienda).filter(Tienda.id_tienda == id_tienda).first()
    if not item:
        raise HTTPException(status_code=HTTP_NOT_FOUND, detail="Tienda no encontrada")
    db.delete(item)
    db.commit()
    return None