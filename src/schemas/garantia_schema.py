# src/schemas/garantia_schema.py
from typing import Optional
from pydantic import BaseModel, Field

class GarantiaBase(BaseModel):
    id_detalle_venta: int
    duracion_meses: int
    tipo_cobertura: str = Field(..., max_length=100)
    estado_garantia: str = Field(..., max_length=50)

class GarantiaCreate(GarantiaBase):
    pass

class GarantiaUpdate(BaseModel):
    id_detalle_venta: Optional[int] = None
    duracion_meses: Optional[int] = None
    tipo_cobertura: Optional[str] = Field(None, max_length=100)
    estado_garantia: Optional[str] = Field(None, max_length=50)

class GarantiaResponse(GarantiaBase):
    id_garantia: int

    class Config:
        from_attributes = True