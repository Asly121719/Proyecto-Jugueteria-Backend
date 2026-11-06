import uuid
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from src.database import Base

class InventarioTienda(Base):
    __tablename__ = "inventario_tiendas"

    id_inventario = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    id_tienda = Column(UUID(as_uuid=True), ForeignKey("tiendas.id_tienda"))
    id_juguete = Column(UUID(as_uuid=True), ForeignKey("juguetes.id_juguete"))
    stock_actual = Column(Integer, nullable=False, default=0)
    pasillo_ubicacion = Column(String(100))

    tienda = relationship("Tienda", back_populates="inventarios")
    juguete = relationship("Juguete", back_populates="inventarios")