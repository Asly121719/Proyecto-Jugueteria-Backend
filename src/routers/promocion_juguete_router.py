from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from uuid import UUID

from src.database import get_db
from src.entities.promocion_juguete import PromocionJuguete
from src.schemas.promocion_juguete_schema import (
    PromocionJugueteCreate,
    PromocionJugueteResponse,
)
from src.utils.constants import (
    HTTP_CREATED,
    HTTP_NO_CONTENT,
    HTTP_NOT_FOUND,
    HTTP_OK,
)

router = APIRouter(prefix="/promocion-juguetes", tags=["Promocion Juguetes"])

@router.get("/", response_model=List[PromocionJugueteResponse], status_code=HTTP_OK)
def obtener_asignaciones(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(PromocionJuguete).offset(skip).limit(limit).all()

@router.post("/", response_model=PromocionJugueteResponse, status_code=HTTP_CREATED)
def crear_asignacion(data: PromocionJugueteCreate, db: Session = Depends(get_db)):
    nueva = PromocionJuguete(**data.dict())
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return nueva

@router.delete("/{id_promocion}/{id_juguete}", status_code=HTTP_NO_CONTENT)
def eliminar_asignacion(id_promocion: UUID, id_juguete: UUID, db: Session = Depends(get_db)):
    item = db.query(PromocionJuguete).filter(
        PromocionJuguete.id_promocion == id_promocion,
        PromocionJuguete.id_juguete == id_juguete
    ).first()
    if not item:
        raise HTTPException(status_code=HTTP_NOT_FOUND, detail="Asignación no encontrada")
    db.delete(item)
    db.commit()
    return None