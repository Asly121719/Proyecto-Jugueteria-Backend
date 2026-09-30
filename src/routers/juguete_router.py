# src/routers/juguete_router.py
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.database import get_db
from src.entities.juguete import Juguete
from src.schemas.juguete_schema import JugueteCreate, JugueteResponse, JugueteUpdate
from src.utils.constants import (
    HTTP_CREATED,
    HTTP_NO_CONTENT,
    HTTP_NOT_FOUND,
    HTTP_OK,
)

router = APIRouter(prefix="/juguetes", tags=["Juguetes"])

@router.get("/", response_model=List[JugueteResponse], status_code=HTTP_OK)
def obtener_juguetes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(Juguete).offset(skip).limit(limit).all()

@router.get("/{id_juguete}", response_model=JugueteResponse, status_code=HTTP_OK)
def obtener_juguete(id_juguete: int, db: Session = Depends(get_db)):
    item = db.query(Juguete).filter(Juguete.id_juguete == id_juguete).first()
    if not item:
        raise HTTPException(status_code=HTTP_NOT_FOUND, detail="Juguete no encontrado")
    return item

@router.post("/", response_model=JugueteResponse, status_code=HTTP_CREATED)
def crear_juguete(data: JugueteCreate, db: Session = Depends(get_db)):
    nuevo = Juguete(**data.dict())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

@router.put("/{id_juguete}", response_model=JugueteResponse, status_code=HTTP_OK)
def actualizar_juguete(id_juguete: int, data: JugueteUpdate, db: Session = Depends(get_db)):
    item = db.query(Juguete).filter(Juguete.id_juguete == id_juguete).first()
    if not item:
        raise HTTPException(status_code=HTTP_NOT_FOUND, detail="Juguete no encontrado")
    for key, value in data.dict(exclude_unset=True).items():
        setattr(item, key, value)
    db.commit()
    db.refresh(item)
    return item

@router.delete("/{id_juguete}", status_code=HTTP_NO_CONTENT)
def eliminar_juguete(id_juguete: int, db: Session = Depends(get_db)):
    item = db.query(Juguete).filter(Juguete.id_juguete == id_juguete).first()
    if not item:
        raise HTTPException(status_code=HTTP_NOT_FOUND, detail="Juguete no encontrado")
    db.delete(item)
    db.commit()
    return None