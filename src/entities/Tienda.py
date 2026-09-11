from src.database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class Tienda(Base):
  _tablename_ = "tiendas"

  id_tienda = Column(Integer, primary_key=True, autoincrement=True)
  nombre_sucursal = Column(String(100), nullable=False)
  direccion = Column(String(255), nullable=False)
  telefono = Column(String(50), nullable=False)
  horario_apertura = Column(String(100), nullable=False)

  empleados = relationship("Empleado", back_populates="tienda")
  inventarios = relationship("InventarioTienda", back_populates="tienda")
  ventas = relationship("Venta", back_populates="tienda")
