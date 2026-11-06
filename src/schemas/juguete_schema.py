from uuid import UUID
from typing import Optional
from pydantic import BaseModel, Field

class JugueteBase(BaseModel):
    id_categoria: UUID
    id_proveedor: UUID
    nombre_producto: str = Field(..., max_length=150)
    precio_unitario: float

class JugueteCreate(JugueteBase):
    pass

class JugueteUpdate(BaseModel):
    id_categoria: Optional[UUID] = None
    id_proveedor: Optional[UUID] = None
    nombre_producto: Optional[str] = Field(None, max_length=150)
    precio_unitario: Optional[float] = None

class JugueteResponse(JugueteBase):
    id_juguete: UUID

    class Config:
        from_attributes = True