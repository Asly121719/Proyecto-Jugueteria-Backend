# src/schemas/cliente_schema.py
from typing import Optional
from pydantic import BaseModel, EmailStr, Field

class ClienteBase(BaseModel):
    nombre: str = Field(..., max_length=100)
    apellido: str = Field(..., max_length=100)
    correo_electronico: EmailStr
    telefono: Optional[str] = Field(None, max_length=50)

class ClienteCreate(ClienteBase):
    pass

class ClienteUpdate(BaseModel):
    nombre: Optional[str] = Field(None, max_length=100)
    apellido: Optional[str] = Field(None, max_length=100)
    correo_electronico: Optional[EmailStr] = None
    telefono: Optional[str] = Field(None, max_length=50)

class ClienteResponse(ClienteBase):
    id_cliente: int

    class Config:
        from_attributes = True