from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.database import get_db
from src.entities.garantias import Garantia
from src.schemas.garantia_schema import (
    GarantiaCreate,
    GarantiaResponse,
    GarantiaUpdate,
)
from src.utils.constants import (
    HTTP_CREATED,
    HTTP_NO_CONTENT,
    HTTP_NOT_FOUND,
    HTTP_OK,
)

router = APIRouter(prefix="/garantias", tags=["Garantías"])

@router.get("/", response_model=List[GarantiaResponse], status_code=HTTP_OK)
def obtener_garantias(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(Garantia).offset(skip).limit(limit).all()

@router.get("/{id_garantia}", response_model=GarantiaResponse, status_code=HTTP_OK)
def obtener_garantia(id_garantia: int, db: Session = Depends(get_db)):
    item = db.query(Garantia).filter(Garantia.id_garantia == id_garantia).first()
    if not item:
        raise HTTPException(status_code=HTTP_NOT_FOUND, detail="Garantía no encontrada")
    return item

@router.post("/", response_model=GarantiaResponse, status_code=HTTP_CREATED)
def crear_garantia(data: GarantiaCreate, db: Session = Depends(get_db)):
    nuevo = Garantia(**data.dict())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

@router.put("/{id_garantia}", response_model=GarantiaResponse, status_code=HTTP_OK)
def actualizar_garantia(id_garantia: int, data: GarantiaUpdate, db: Session = Depends(get_db)):
    item = db.query(Garantia).filter(Garantia.id_garantia == id_garantia).first()
    if not item:
        raise HTTPException(status_code=HTTP_NOT_FOUND, detail="Garantía no encontrada")
    for key, value in data.dict(exclude_unset=True).items():
        setattr(item, key, value)
    db.commit()
    db.refresh(item)
    return item

@router.delete("/{id_garantia}", status_code=HTTP_NO_CONTENT)
def eliminar_garantia(id_garantia: int, db: Session = Depends(get_db)):
    item = db.query(Garantia).filter(Garantia.id_garantia == id_garantia).first()
    if not item:
        raise HTTPException(status_code=HTTP_NOT_FOUND, detail="Garantía no encontrada")
    db.delete(item)
    db.commit()
    return None