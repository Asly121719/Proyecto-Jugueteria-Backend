from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.database import get_db
from src.entities.promocion import Promocion
from src.schemas.promocion_schema import (
    PromocionCreate,
    PromocionResponse,
    PromocionUpdate,
)
from src.utils.constants import (
    HTTP_CREATED,
    HTTP_NO_CONTENT,
    HTTP_NOT_FOUND,
    HTTP_OK,
)

router = APIRouter(prefix="/promociones", tags=["Promociones"])

@router.get("/", response_model=List[PromocionResponse], status_code=HTTP_OK)
def obtener_promociones(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(Promocion).offset(skip).limit(limit).all()

@router.get("/{id_promocion}", response_model=PromocionResponse, status_code=HTTP_OK)
def obtener_promocion(id_promocion: int, db: Session = Depends(get_db)):
    item = db.query(Promocion).filter(Promocion.id_promocion == id_promocion).first()
    if not item:
        raise HTTPException(status_code=HTTP_NOT_FOUND, detail="Promoción no encontrada")
    return item

@router.post("/", response_model=PromocionResponse, status_code=HTTP_CREATED)
def crear_promocion(data: PromocionCreate, db: Session = Depends(get_db)):
    nuevo = Promocion(**data.dict())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

@router.put("/{id_promocion}", response_model=PromocionResponse, status_code=HTTP_OK)
def actualizar_promocion(id_promocion: int, data: PromocionUpdate, db: Session = Depends(get_db)):
    item = db.query(Promocion).filter(Promocion.id_promocion == id_promocion).first()
    if not item:
        raise HTTPException(status_code=HTTP_NOT_FOUND, detail="Promoción no encontrada")
    for key, value in data.dict(exclude_unset=True).items():
        setattr(item, key, value)
    db.commit()
    db.refresh(item)
    return item

@router.delete("/{id_promocion}", status_code=HTTP_NO_CONTENT)
def eliminar_promocion(id_promocion: int, db: Session = Depends(get_db)):
    item = db.query(Promocion).filter(Promocion.id_promocion == id_promocion).first()
    if not item:
        raise HTTPException(status_code=HTTP_NOT_FOUND, detail="Promoción no encontrada")
    db.delete(item)
    db.commit()
    return None