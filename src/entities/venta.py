from sqlalchemy import Column, DateTime, ForeignKey, Numeric
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid
from datetime import datetime
from src.database import Base

class Venta(Base):
    __tablename__ = "ventas"
    __table_args__ = {'extend_existing': True}

    id_venta = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    id_tienda = Column(UUID(as_uuid=True), ForeignKey("tiendas.id_tienda"), nullable=False)
    id_empleado = Column(UUID(as_uuid=True), ForeignKey("empleados.id_empleado"), nullable=False)
    id_cliente = Column(UUID(as_uuid=True), ForeignKey("clientes.id_cliente"), nullable=False)
    fecha_hora_venta = Column(DateTime, default=datetime.utcnow, nullable=False)
    total = Column(Numeric(10, 2), nullable=False, default=0.00)

    cliente = relationship("Cliente")
    tienda = relationship("Tienda")
    empleado = relationship("Empleado")
    detalles = relationship("DetalleVenta", back_populates="venta", cascade="all, delete-orphan")