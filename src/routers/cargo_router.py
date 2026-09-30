# src/routers/cargo_router.py
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.database import get_db
from src.entities.cargo import Cargo
from src.schemas.cargo_schema import CargoCreate, CargoResponse, CargoUpdate
from src.utils.constants import (
    HTTP_CREATED,
    HTTP_NO_CONTENT,
    HTTP_NOT_FOUND,
    HTTP_OK,
)

router = APIRouter(prefix="/cargos", tags=["Cargos"])

@router.get("/", response_model=List[CargoResponse], status_code=HTTP_OK)
def obtener_cargos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(Cargo).offset(skip).limit(limit).all()

@router.get("/{id_cargo}", response_model=CargoResponse, status_code=HTTP_OK)
def obtener_cargo(id_cargo: int, db: Session = Depends(get_db)):
    item = db.query(Cargo).filter(Cargo.id_cargo == id_cargo).first()
    if not item:
        raise HTTPException(status_code=HTTP_NOT_FOUND, detail="Cargo no encontrado")
    return item

@router.post("/", response_model=CargoResponse, status_code=HTTP_CREATED)
def crear_cargo(data: CargoCreate, db: Session = Depends(get_db)):
    nuevo = Cargo(**data.dict())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

@router.put("/{id_cargo}", response_model=CargoResponse, status_code=HTTP_OK)
def actualizar_cargo(id_cargo: int, data: CargoUpdate, db: Session = Depends(get_db)):
    item = db.query(Cargo).filter(Cargo.id_cargo == id_cargo).first()
    if not item:
        raise HTTPException(status_code=HTTP_NOT_FOUND, detail="Cargo no encontrado")
    for key, value in data.dict(exclude_unset=True).items():
        setattr(item, key, value)
    db.commit()
    db.refresh(item)
    return item

@router.delete("/{id_cargo}", status_code=HTTP_NO_CONTENT)
def eliminar_cargo(id_cargo: int, db: Session = Depends(get_db)):
    item = db.query(Cargo).filter(Cargo.id_cargo == id_cargo).first()
    if not item:
        raise HTTPException(status_code=HTTP_NOT_FOUND, detail="Cargo no encontrado")
    db.delete(item)
    db.commit()
    return None