from uuid import UUID
from typing import Optional
from pydantic import BaseModel, Field

class InventarioBase(BaseModel):
    id_tienda: UUID
    id_juguete: UUID
    stock_actual: int
    pasillo_ubicacion: Optional[str] = Field(None, max_length=100)

class InventarioCreate(InventarioBase):
    pass

class InventarioUpdate(BaseModel):
    id_tienda: Optional[UUID] = None
    id_juguete: Optional[UUID] = None
    stock_actual: Optional[int] = None
    pasillo_ubicacion: Optional[str] = Field(None, max_length=100)

class InventarioResponse(InventarioBase):
    id_inventario: UUID

    class Config:
        from_attributes = True