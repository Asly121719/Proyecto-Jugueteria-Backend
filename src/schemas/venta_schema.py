# src/schemas/venta_schema.py
from typing import Optional
from pydantic import BaseModel, Field

class VentaBase(BaseModel):
    id_tienda: int
    id_empleado: int
    id_cliente: Optional[int] = None
    fecha_hora_venta: str = Field(..., max_length=50)

class VentaCreate(VentaBase):
    pass

class VentaUpdate(BaseModel):
    id_tienda: Optional[int] = None
    id_empleado: Optional[int] = None
    id_cliente: Optional[int] = None
    fecha_hora_venta: Optional[str] = Field(None, max_length=50)

class VentaResponse(VentaBase):
    id_venta: int

    class Config:
        from_attributes = True