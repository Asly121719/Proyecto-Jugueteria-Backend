from src.database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class Proveedor(Base):
  __tablename__ = "proveedores"

  id_proveedor = Column(Integer, primary_key=True, autoincrement=True)
  razon_social = Column(String(150), nullable=False)
  nombre_contacto = Column(String(100))
  telefono = Column(String(50))
  pais_origen = Column(String(100))

  juguetes = relationship("Juguete", back_populates="proveedor")