# src/schemas/proveedor_schema.py
from typing import Optional
from pydantic import BaseModel, Field

class ProveedorBase(BaseModel):
    razon_social: str = Field(..., max_length=150)
    nombre_contacto: Optional[str] = Field(None, max_length=100)
    telefono: Optional[str] = Field(None, max_length=50)
    pais_origen: Optional[str] = Field(None, max_length=100)

class ProveedorCreate(ProveedorBase):
    pass

class ProveedorUpdate(BaseModel):
    razon_social: Optional[str] = Field(None, max_length=150)
    nombre_contacto: Optional[str] = Field(None, max_length=100)
    telefono: Optional[str] = Field(None, max_length=50)
    pais_origen: Optional[str] = Field(None, max_length=100)

class ProveedorResponse(ProveedorBase):
    id_proveedor: int

    class Config:
        from_attributes = True