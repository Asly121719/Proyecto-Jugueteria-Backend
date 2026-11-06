import uuid
from sqlalchemy import Column, Numeric, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from src.database import Base
from .juguete import promocion_juguetes

class Promocion(Base):
    __tablename__ = "promociones"

    id_promocion = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    nombre_campana = Column(String(150), nullable=False)
    porcentaje_descuento = Column(Numeric(5, 2), nullable=False)
    fecha_inicio = Column(String(50), nullable=False)
    fecha_fin = Column(String(50), nullable=False)

    juguetes = relationship("Juguete", secondary=promocion_juguetes, back_populates="promociones")