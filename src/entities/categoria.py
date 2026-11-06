import uuid
from sqlalchemy import Boolean, Column, String, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from src.database import Base

class Categoria(Base):
    __tablename__ = "categorias"

    id_categoria = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    nombre_categoria = Column(String(100), nullable=False)
    descripcion = Column(Text)
    edad_recomendada = Column(String(50))
    es_electrico = Column(Boolean, default=False)

    juguetes = relationship("Juguete", back_populates="categoria")