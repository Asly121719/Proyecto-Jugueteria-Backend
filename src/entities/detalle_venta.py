import uuid
from sqlalchemy import Column, ForeignKey, Integer, Numeric
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from src.database import Base

class DetalleVenta(Base):
    __tablename__ = "detalle_ventas"
    __table_args__ = {"extend_existing": True}

    id_detalle = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    id_venta = Column(UUID(as_uuid=True), ForeignKey("ventas.id_venta"))
    id_juguete = Column(UUID(as_uuid=True), ForeignKey("juguetes.id_juguete"))
    cantidad_comprada = Column(Integer, nullable=False)
    subtotal = Column(Numeric(10, 2), nullable=False)

    venta = relationship("Venta", back_populates="detalles")
    juguete = relationship("Juguete", back_populates="detalles")
    garantias = relationship("Garantia", back_populates="detalle_venta")