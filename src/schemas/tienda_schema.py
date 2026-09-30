# src/schemas/tienda_schema.py
from typing import Optional
from pydantic import BaseModel, Field

class TiendaBase(BaseModel):
    nombre_sucursal: str = Field(..., max_length=100)
    direccion: str = Field(..., max_length=255)
    telefono: str = Field(..., max_length=50)
    horario_apertura: str = Field(..., max_length=100)

class TiendaCreate(TiendaBase):
    pass

class TiendaUpdate(BaseModel):
    nombre_sucursal: Optional[str] = Field(None, max_length=100)
    direccion: Optional[str] = Field(None, max_length=255)
    telefono: Optional[str] = Field(None, max_length=50)
    horario_apertura: Optional[str] = Field(None, max_length=100)

class TiendaResponse(TiendaBase):
    id_tienda: int

    class Config:
        from_attributes = True