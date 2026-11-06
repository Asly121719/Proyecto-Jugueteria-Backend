import uuid
from src.database import Base
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship


class Garantia(Base):
    __tablename__ = "garantias"

    id_garantia = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, index=True)
    id_detalle_venta = Column(UUID(as_uuid=True), ForeignKey("detalle_ventas.id_detalle"), nullable=False)
    duracion_meses = Column(Integer, nullable=False)
    tipo_cobertura = Column(String(100), nullable=False)
    estado_garantia = Column(String(50), nullable=False)

    detalle_venta = relationship("DetalleVenta", back_populates="garantias")