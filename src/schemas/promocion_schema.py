# src/schemas/promocion_schema.py
from typing import Optional
from pydantic import BaseModel, Field

class PromocionBase(BaseModel):
    nombre_campana: str = Field(..., max_length=150)
    porcentaje_descuento: float
    fecha_inicio: str = Field(..., max_length=50)
    fecha_fin: str = Field(..., max_length=50)

class PromocionCreate(PromocionBase):
    pass

class PromocionUpdate(BaseModel):
    nombre_campana: Optional[str] = Field(None, max_length=150)
    porcentaje_descuento: Optional[float] = None
    fecha_inicio: Optional[str] = Field(None, max_length=50)
    fecha_fin: Optional[str] = Field(None, max_length=50)

class PromocionResponse(PromocionBase):
    id_promocion: int

    class Config:
        from_attributes = True