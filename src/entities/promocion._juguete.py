from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from src.database import Base

class PromocionJuguete(Base):
    __tablename__ = "promocion_juguetes"

    id_promocion = Column(UUID(as_uuid=True), ForeignKey("promociones.id_promocion"), primary_key=True, nullable=False)
    id_juguete = Column(UUID(as_uuid=True), ForeignKey("juguetes.id_juguete"), primary_key=True, nullable=False)