from src.database import Base
from sqlalchemy import Column, Integer, Numeric, String
from sqlalchemy.orm import relationship
from .juguete import promocion_juguetes


class Promocion(Base):
  __tablename__ = "promociones"

  id_promocion = Column(Integer, primary_key=True, autoincrement=True)
  nombre_campana = Column(String(150), nullable=False)
  porcentaje_descuento = Column(Numeric(5, 2), nullable=False)
  fecha_inicio = Column(String(50), nullable=False)
  fecha_fin = Column(String(50), nullable=False)

  juguetes = relationship(
      "Juguete", secondary=promocion_juguetes, back_populates="promociones"
  )