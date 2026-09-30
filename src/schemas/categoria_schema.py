# src/schemas/categoria_schema.py
from typing import Optional
from pydantic import BaseModel, Field

class CategoriaBase(BaseModel):
    nombre_categoria: str = Field(..., max_length=100)
    descripcion: Optional[str] = None
    edad_recomendada: Optional[str] = Field(None, max_length=50)
    es_electrico: Optional[bool] = False

class CategoriaCreate(CategoriaBase):
    pass

class CategoriaUpdate(BaseModel):
    nombre_categoria: Optional[str] = Field(None, max_length=100)
    descripcion: Optional[str] = None
    edad_recomendada: Optional[str] = Field(None, max_length=50)
    es_electrico: Optional[bool] = None

class CategoriaResponse(CategoriaBase):
    id_categoria: int

    class Config:
        from_attributes = True