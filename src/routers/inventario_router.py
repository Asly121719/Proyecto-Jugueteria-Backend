from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.database import get_db
from src.entities.inventario import InventarioTienda
from src.schemas.inventario_schema import (
    InventarioCreate,
    InventarioResponse,
    InventarioUpdate,
)
from src.utils.constants import (
    HTTP_CREATED,
    HTTP_NO_CONTENT,
    HTTP_NOT_FOUND,
    HTTP_OK,
)

router = APIRouter(prefix="/inventario", tags=["Inventario Tiendas"])

@router.get("/", response_model=List[InventarioResponse], status_code=HTTP_OK)
def obtener_inventarios(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(InventarioTienda).offset(skip).limit(limit).all()

@router.get("/{id_inventario}", response_model=InventarioResponse, status_code=HTTP_OK)
def obtener_inventario(id_inventario: int, db: Session = Depends(get_db)):
    item = db.query(InventarioTienda).filter(InventarioTienda.id_inventario == id_inventario).first()
    if not item:
        raise HTTPException(status_code=HTTP_NOT_FOUND, detail="Registro de inventario no encontrado")
    return item

@router.post("/", response_model=InventarioResponse, status_code=HTTP_CREATED)
def crear_inventario(data: InventarioCreate, db: Session = Depends(get_db)):
    nuevo = InventarioTienda(**data.dict())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

@router.put("/{id_inventario}", response_model=InventarioResponse, status_code=HTTP_OK)
def actualizar_inventario(id_inventario: int, data: InventarioUpdate, db: Session = Depends(get_db)):
    item = db.query(InventarioTienda).filter(InventarioTienda.id_inventario == id_inventario).first()
    if not item:
        raise HTTPException(status_code=HTTP_NOT_FOUND, detail="Registro de inventario no encontrado")
    for key, value in data.dict(exclude_unset=True).items():
        setattr(item, key, value)
    db.commit()
    db.refresh(item)
    return item

@router.delete("/{id_inventario}", status_code=HTTP_NO_CONTENT)
def eliminar_inventario(id_inventario: int, db: Session = Depends(get_db)):
    item = db.query(InventarioTienda).filter(InventarioTienda.id_inventario == id_inventario).first()
    if not item:
        raise HTTPException(status_code=HTTP_NOT_FOUND, detail="Registro de inventario no encontrado")
    db.delete(item)
    db.commit()
    return None