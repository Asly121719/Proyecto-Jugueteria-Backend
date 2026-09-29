from src.database import Base
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class Empleado(Base):
  __tablename__ = "empleados"

  id_empleado = Column(Integer, primary_key=True, autoincrement=True)
  id_tienda = Column(Integer, ForeignKey("tiendas.id_tienda"))
  id_cargo = Column(Integer, ForeignKey("cargos.id_cargo"))
  nombre = Column(String(100), nullable=False)
  apellido = Column(String(100), nullable=False)
  correo_electronico = Column(String(150), unique=True, nullable=False)

  tienda = relationship("Tienda", back_populates="empleados")
  cargo = relationship("Cargo", back_populates="empleados")
  ventas = relationship("Venta", back_populates="empleado")