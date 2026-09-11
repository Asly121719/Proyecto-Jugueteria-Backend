from src.database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class Cliente(Base):
  _tablename_ = "clientes"

  id_cliente = Column(Integer, primary_key=True, autoincrement=True)
  nombre = Column(String(100), nullable=False)
  apellido = Column(String(100), nullable=False)
  correo_electronico = Column(String(150), unique=True, nullable=False)
  telefono = Column(String(50))

  ventas = relationship("Venta", back_populates="cliente")