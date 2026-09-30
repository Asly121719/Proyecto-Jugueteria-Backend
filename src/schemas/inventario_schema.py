# src/schemas/inventario_schema.py
from typing import Optional
from pydantic import BaseModel, Field

class InventarioBase(BaseModel):
    id_tienda: int
    id_juguete: int
    stock_actual: int
    pasillo_ubicacion: Optional[str] = Field(None, max_length=100)

class InventarioCreate(InventarioBase):
    pass

class InventarioUpdate(BaseModel):
    id_tienda: Optional[int] = None
    id_juguete: Optional[int] = None
    stock_actual: Optional[int] = None
    pasillo_ubicacion: Optional[str] = Field(None, max_length=100)

class InventarioResponse(InventarioBase):
    id_inventario: int

    class Config:
        from_attributes = True