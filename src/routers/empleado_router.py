# src/routers/empleado_router.py
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.database import get_db
from src.entities.Empleado import Empleado
from src.schemas.empleado_schema import (
    EmpleadoCreate,
    EmpleadoResponse,
    EmpleadoUpdate,
)
from src.utils.constants import (
    HTTP_CREATED,
    HTTP_NO_CONTENT,
    HTTP_NOT_FOUND,
    HTTP_OK,
)

router = APIRouter(prefix="/empleados", tags=["Empleados"])

@router.get("/", response_model=List[EmpleadoResponse], status_code=HTTP_OK)
def obtener_empleados(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(Empleado).offset(skip).limit(limit).all()

@router.get("/{id_empleado}", response_model=EmpleadoResponse, status_code=HTTP_OK)
def obtener_empleado(id_empleado: int, db: Session = Depends(get_db)):
    item = db.query(Empleado).filter(Empleado.id_empleado == id_empleado).first()
    if not item:
        raise HTTPException(status_code=HTTP_NOT_FOUND, detail="Empleado no encontrado")
    return item

@router.post("/", response_model=EmpleadoResponse, status_code=HTTP_CREATED)
def crear_empleado(data: EmpleadoCreate, db: Session = Depends(get_db)):
    nuevo = Empleado(**data.dict())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

@router.put("/{id_empleado}", response_model=EmpleadoResponse, status_code=HTTP_OK)
def actualizar_empleado(id_empleado: int, data: EmpleadoUpdate, db: Session = Depends(get_db)):
    item = db.query(Empleado).filter(Empleado.id_empleado == id_empleado).first()
    if not item:
        raise HTTPException(status_code=HTTP_NOT_FOUND, detail="Empleado no encontrado")
    for key, value in data.dict(exclude_unset=True).items():
        setattr(item, key, value)
    db.commit()
    db.refresh(item)
    return item

@router.delete("/{id_empleado}", status_code=HTTP_NO_CONTENT)
def eliminar_empleado(id_empleado: int, db: Session = Depends(get_db)):
    item = db.query(Empleado).filter(Empleado.id_empleado == id_empleado).first()
    if not item:
        raise HTTPException(status_code=HTTP_NOT_FOUND, detail="Empleado no encontrado")
    db.delete(item)
    db.commit()
    return None