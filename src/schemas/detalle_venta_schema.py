from uuid import UUID
from typing import Optional
from pydantic import BaseModel

class DetalleVentaBase(BaseModel):
    id_venta: UUID
    id_juguete: UUID
    cantidad_comprada: int
    subtotal: float

class DetalleVentaCreate(DetalleVentaBase):
    pass

class DetalleVentaUpdate(BaseModel):
    id_venta: Optional[UUID] = None
    id_juguete: Optional[UUID] = None
    cantidad_comprada: Optional[int] = None
    subtotal: Optional[float] = None

class DetalleVentaResponse(DetalleVentaBase):
    id_detalle: UUID

    class Config:
        from_attributes = True