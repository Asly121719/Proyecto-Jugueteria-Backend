from src.database import Base
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

class Garantia(Base):
  __tablename__ = "garantias"

  id_garantia = Column(Integer, primary_key=True, autoincrement=True)
  id_detalle_venta = Column(Integer, ForeignKey("detalle_ventas.id_detalle"))
  duracion_meses = Column(Integer, nullable=False)
  tipo_cobertura = Column(String(100), nullable=False)
  estado_garantia = Column(String(50), nullable=False)

  detalle_venta = relationship("DetalleVenta", back_populates="garantias")                                                                                                                                                                                                                 from src.database import Base
