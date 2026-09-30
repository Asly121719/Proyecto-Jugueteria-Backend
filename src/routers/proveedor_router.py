from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.database import get_db
from src.entities.Proveedor import Proveedor
from src.schemas.proveedor_schema import (
    ProveedorCreate,
    ProveedorResponse,
    ProveedorUpdate,
)
from src.utils.constants import (
    HTTP_CREATED,
    HTTP_NO_CONTENT,
    HTTP_NOT_FOUND,
    HTTP_OK,
)

router = APIRouter(prefix="/proveedores", tags=["Proveedores"])

@router.get("/", response_model=List[ProveedorResponse], status_code=HTTP_OK)
def obtener_proveedores(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(Proveedor).offset(skip).limit(limit).all()

@router.get("/{id_proveedor}", response_model=ProveedorResponse, status_code=HTTP_OK)
def obtener_proveedor(id_proveedor: int, db: Session = Depends(get_db)):
    item = db.query(Proveedor).filter(Proveedor.id_proveedor == id_proveedor).first()
    if not item:
        raise HTTPException(status_code=HTTP_NOT_FOUND, detail="Proveedor no encontrado")
    return item

@router.post("/", response_model=ProveedorResponse, status_code=HTTP_CREATED)
def crear_proveedor(data: ProveedorCreate, db: Session = Depends(get_db)):
    nuevo = Proveedor(**data.dict())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

@router.put("/{id_proveedor}", response_model=ProveedorResponse, status_code=HTTP_OK)
def actualizar_proveedor(id_proveedor: int, data: ProveedorUpdate, db: Session = Depends(get_db)):
    item = db.query(Proveedor).filter(Proveedor.id_proveedor == id_proveedor).first()
    if not item:
        raise HTTPException(status_code=HTTP_NOT_FOUND, detail="Proveedor no encontrado")
    for key, value in data.dict(exclude_unset=True).items():
        setattr(item, key, value)
    db.commit()
    db.refresh(item)
    return item

@router.delete("/{id_proveedor}", status_code=HTTP_NO_CONTENT)
def eliminar_proveedor(id_proveedor: int, db: Session = Depends(get_db)):
    item = db.query(Proveedor).filter(Proveedor.id_proveedor == id_proveedor).first()
    if not item:
        raise HTTPException(status_code=HTTP_NOT_FOUND, detail="Proveedor no encontrado")
    db.delete(item)
    db.commit()
    return None