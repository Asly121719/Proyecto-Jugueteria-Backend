# src/schemas/detalle_venta_schema.py
from typing import Optional
from pydantic import BaseModel

class DetalleVentaBase(BaseModel):
    id_venta: int
    id_juguete: int
    cantidad_comprada: int
    subtotal: float

class DetalleVentaCreate(DetalleVentaBase):
    pass

class DetalleVentaUpdate(BaseModel):
    id_venta: Optional[int] = None
    id_juguete: Optional[int] = None
    cantidad_comprada: Optional[int] = None
    subtotal: Optional[float] = None

class DetalleVentaResponse(DetalleVentaBase):
    id_detalle: int

    class Config:
        from_attributes = True