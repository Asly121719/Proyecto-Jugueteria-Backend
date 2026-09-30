# src/schemas/juguete_schema.py
from typing import Optional
from pydantic import BaseModel, Field

class JugueteBase(BaseModel):
    id_categoria: int
    id_proveedor: int
    nombre_producto: str = Field(..., max_length=150)
    precio_unitario: float

class JugueteCreate(JugueteBase):
    pass

class JugueteUpdate(BaseModel):
    id_categoria: Optional[int] = None
    id_proveedor: Optional[int] = None
    nombre_producto: Optional[str] = Field(None, max_length=150)
    precio_unitario: Optional[float] = None

class JugueteResponse(JugueteBase):
    id_juguete: int

    class Config:
        from_attributes = True