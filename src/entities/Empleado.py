import uuid
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from src.database import Base

class Empleado(Base):
    __tablename__ = "empleados"

    id_empleado = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    id_tienda = Column(UUID(as_uuid=True), ForeignKey("tiendas.id_tienda"))
    id_cargo = Column(UUID(as_uuid=True), ForeignKey("cargos.id_cargo"))
    nombre = Column(String(100), nullable=False)
    apellido = Column(String(100), nullable=False)
    correo_electronico = Column(String(150), unique=True, nullable=False)

    tienda = relationship("Tienda", back_populates="empleados")
    cargo = relationship("Cargo", back_populates="empleados")
    ventas = relationship("Venta", back_populates="empleado")