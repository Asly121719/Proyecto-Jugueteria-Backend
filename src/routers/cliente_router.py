from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.database import get_db
from src.entities.cliente import Cliente
from src.schemas.cliente_schema import ClienteCreate, ClienteResponse, ClienteUpdate
from src.utils.constants import (
    HTTP_BAD_REQUEST,
    HTTP_CREATED,
    HTTP_NO_CONTENT,
    HTTP_NOT_FOUND,
    HTTP_OK,
)

router = APIRouter(prefix="/clientes", tags=["Clientes"])

@router.get("/", response_model=List[ClienteResponse], status_code=HTTP_OK)
def obtener_clientes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(Cliente).offset(skip).limit(limit).all()

@router.get("/{id_cliente}", response_model=ClienteResponse, status_code=HTTP_OK)
def obtener_cliente(id_cliente: int, db: Session = Depends(get_db)):
    item = db.query(Cliente).filter(Cliente.id_cliente == id_cliente).first()
    if not item:
        raise HTTPException(status_code=HTTP_NOT_FOUND, detail="Cliente no encontrado")
    return item

@router.post("/", response_model=ClienteResponse, status_code=HTTP_CREATED)
def crear_cliente(data: ClienteCreate, db: Session = Depends(get_db)):
    existe = db.query(Cliente).filter(Cliente.correo_electronico == data.correo_electronico).first()
    if existe:
        raise HTTPException(status_code=HTTP_BAD_REQUEST, detail="El correo ya está registrado")
    nuevo = Cliente(**data.dict())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

@router.put("/{id_cliente}", response_model=ClienteResponse, status_code=HTTP_OK)
def actualizar_cliente(id_cliente: int, data: ClienteUpdate, db: Session = Depends(get_db)):
    item = db.query(Cliente).filter(Cliente.id_cliente == id_cliente).first()
    if not item:
        raise HTTPException(status_code=HTTP_NOT_FOUND, detail="Cliente no encontrado")
    for key, value in data.dict(exclude_unset=True).items():
        setattr(item, key, value)
    db.commit()
    db.refresh(item)
    return item

@router.delete("/{id_cliente}", status_code=HTTP_NO_CONTENT)
def eliminar_cliente(id_cliente: int, db: Session = Depends(get_db)):
    item = db.query(Cliente).filter(Cliente.id_cliente == id_cliente).first()
    if not item:
        raise HTTPException(status_code=HTTP_NOT_FOUND, detail="Cliente no encontrado")
    db.delete(item)
    db.commit()
    return None