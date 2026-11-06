import uuid
from sqlalchemy import Column, ForeignKey, Numeric, String, Table
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from src.database import Base

promocion_juguetes = Table(
    "promocion_juguetes",
    Base.metadata,
    Column("id_promocion", UUID(as_uuid=True), ForeignKey("promociones.id_promocion"), primary_key=True),
    Column("id_juguete", UUID(as_uuid=True), ForeignKey("juguetes.id_juguete"), primary_key=True),
    extend_existing=True,
)

class Juguete(Base):
    __tablename__ = "juguetes"

    id_juguete = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    id_categoria = Column(UUID(as_uuid=True), ForeignKey("categorias.id_categoria"))
    id_proveedor = Column(UUID(as_uuid=True), ForeignKey("proveedores.id_proveedor"))
    nombre_producto = Column(String(150), nullable=False)
    precio_unitario = Column(Numeric(10, 2), nullable=False)

    detalles = relationship("DetalleVenta", back_populates="juguete")
    categoria = relationship("Categoria", back_populates="juguetes")
    proveedor = relationship("Proveedor", back_populates="juguetes")
    inventarios = relationship("InventarioTienda", back_populates="juguete")
    promociones = relationship("Promocion", secondary=promocion_juguetes, back_populates="juguetes")