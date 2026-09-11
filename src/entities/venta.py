from src.database import Base
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class Venta(Base):
  _tablename_ = "ventas"

  id_venta = Column(Integer, primary_key=True, autoincrement=True)
  id_tienda = Column(Integer, ForeignKey("tiendas.id_tienda"))
  id_empleado = Column(Integer, ForeignKey("empleados.id_empleado"))
  id_cliente = Column(Integer, ForeignKey("clientes.id_cliente"), nullable=True)
  fecha_hora_venta = Column(String(50), nullable=False)

  tienda = relationship("Tienda", back_populates="ventas")
  empleado = relationship("Empleado", back_populates="ventas")
  cliente = relationship("Cliente", back_populates="ventas")
  detalles = relationship(
      "DetalleVenta", back_populates="venta", cascade="all, delete-orphan"
  )
  envio_online = relationship(
      "EnvioOnline",
      uselist=False,
      back_populates="venta",
      cascade="all, delete-orphan",
  )
