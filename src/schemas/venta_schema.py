from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from typing import List, Optional

class DetalleVentaCreate(BaseModel):
    id_juguete: UUID
    cantidad_comprada: int

class VentaCreate(BaseModel):
    id_tienda: UUID
    id_empleado: UUID
    id_cliente: UUID
    fecha_hora_venta: Optional[datetime] = None
    detalles: List[DetalleVentaCreate] # 👈 Recibe los productos seleccionados en el form

class VentaResponse(BaseModel):
    id_venta: UUID
    id_tienda: UUID
    id_empleado: UUID
    id_cliente: UUID
    fecha_hora_venta: datetime
    total: float

    class Config:
        from_attributes = True