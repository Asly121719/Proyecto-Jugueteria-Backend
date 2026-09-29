from src.database import Base
from sqlalchemy import Column, ForeignKey, Integer, Numeric
from sqlalchemy.orm import relationship


class DetalleVenta(Base):
  __tablename__ = "detalle_ventas"
  __table_args__ = {
      "extend_existing": True
      }

  id_detalle = Column(Integer, primary_key=True, autoincrement=True)
  id_venta = Column(Integer, ForeignKey("ventas.id_venta"))
  id_juguete = Column(Integer, ForeignKey("juguetes.id_juguete"))
  cantidad_comprada = Column(Integer, nullable=False)
  subtotal = Column(Numeric(10, 2), nullable=False)

  venta = relationship("Venta", back_populates="detalles")
  juguete = relationship("Juguete", back_populates="detalles")
  garantias = relationship("Garantia", back_populates="detalle_venta")