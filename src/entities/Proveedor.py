import uuid
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from src.database import Base

class Proveedor(Base):
    __tablename__ = "proveedores"

    id_proveedor = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    razon_social = Column(String(150), nullable=False)
    nombre_contacto = Column(String(100))
    telefono = Column(String(50))
    pais_origen = Column(String(100))

    juguetes = relationship("Juguete", back_populates="proveedor")