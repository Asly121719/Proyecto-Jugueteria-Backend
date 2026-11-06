from uuid import UUID
from typing import Optional
from pydantic import BaseModel, EmailStr, Field

class EmpleadoBase(BaseModel):
    id_tienda: UUID
    id_cargo: UUID
    nombre: str = Field(..., max_length=100)
    apellido: str = Field(..., max_length=100)
    correo_electronico: EmailStr

class EmpleadoCreate(EmpleadoBase):
    pass

class EmpleadoUpdate(BaseModel):
    id_tienda: Optional[UUID] = None
    id_cargo: Optional[UUID] = None
    nombre: Optional[str] = Field(None, max_length=100)
    apellido: Optional[str] = Field(None, max_length=100)
    correo_electronico: Optional[EmailStr] = None

class EmpleadoResponse(EmpleadoBase):
    id_empleado: UUID

    class Config:
        from_attributes = True