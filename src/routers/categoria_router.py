from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.database import get_db
from src.entities.categoria import Categoria
from src.schemas.categoria_schema import (
    CategoriaCreate,
    CategoriaResponse,
    CategoriaUpdate,
)
from src.utils.constants import (
    HTTP_BAD_REQUEST,
    HTTP_CREATED,
    HTTP_NO_CONTENT,
    HTTP_NOT_FOUND,
    HTTP_OK,
)

router = APIRouter(prefix="/categorias", tags=["Categorías"])

@router.get("/", response_model=List[CategoriaResponse], status_code=HTTP_OK)
def obtener_categorias(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(Categoria).offset(skip).limit(limit).all()

@router.get("/{id_categoria}", response_model=CategoriaResponse, status_code=HTTP_OK)
def obtener_categoria(id_categoria: int, db: Session = Depends(get_db)):
    item = db.query(Categoria).filter(Categoria.id_categoria == id_categoria).first()
    if not item:
        raise HTTPException(status_code=HTTP_NOT_FOUND, detail="Categoría no encontrada")
    return item

@router.post("/", response_model=CategoriaResponse, status_code=HTTP_CREATED)
def crear_categoria(data: CategoriaCreate, db: Session = Depends(get_db)):
    nuevo = Categoria(**data.dict())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

@router.put("/{id_categoria}", response_model=CategoriaResponse, status_code=HTTP_OK)
def actualizar_categoria(id_categoria: int, data: CategoriaUpdate, db: Session = Depends(get_db)):
    item = db.query(Categoria).filter(Categoria.id_categoria == id_categoria).first()
    if not item:
        raise HTTPException(status_code=HTTP_NOT_FOUND, detail="Categoría no encontrada")
    for key, value in data.dict(exclude_unset=True).items():
        setattr(item, key, value)
    db.commit()
    db.refresh(item)
    return item

@router.delete("/{id_categoria}", status_code=HTTP_NO_CONTENT)
def eliminar_categoria(id_categoria: int, db: Session = Depends(get_db)):
    item = db.query(Categoria).filter(Categoria.id_categoria == id_categoria).first()
    if not item:
        raise HTTPException(status_code=HTTP_NOT_FOUND, detail="Categoría no encontrada")
    db.delete(item)
    db.commit()
    return None