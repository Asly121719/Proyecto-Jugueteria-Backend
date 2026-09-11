from src.database import Base
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class InventarioTienda(Base):
  __tablename__ = "inventario_tiendas"

  id_inventario = Column(Integer, primary_key=True, autoincrement=True)
  id_tienda = Column(Integer, ForeignKey("tiendas.id_tienda"))
  id_juguete = Column(Integer, ForeignKey("juguetes.id_juguete"))
  stock_actual = Column(Integer, nullable=False, default=0)
  pasillo_ubicacion = Column(String(100))

  tienda = relationship("Tienda", back_populates="inventarios")
  juguete = relationship("Juguete", back_populates="inventarios")