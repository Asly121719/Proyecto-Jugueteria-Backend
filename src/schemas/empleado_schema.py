# src/schemas/empleado_schema.py
from typing import Optional
from pydantic import BaseModel, EmailStr, Field

class EmpleadoBase(BaseModel):
    id_tienda: int
    id_cargo: int
    nombre: str = Field(..., max_length=100)
    apellido: str = Field(..., max_length=100)
    correo_electronico: EmailStr

class EmpleadoCreate(EmpleadoBase):
    pass

class EmpleadoUpdate(BaseModel):
    id_tienda: Optional[int] = None
    id_cargo: Optional[int] = None
    nombre: Optional[str] = Field(None, max_length=100)
    apellido: Optional[str] = Field(None, max_length=100)
    correo_electronico: Optional[EmailStr] = None

class EmpleadoResponse(EmpleadoBase):
    id_empleado: int

    class Config:
        from_attributes = True