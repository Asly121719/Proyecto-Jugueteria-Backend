from src.database import Base
from sqlalchemy import Boolean, Column, Integer, String, Text
from sqlalchemy.orm import relationship


class Categoria(Base):
  _tablename_ = "categorias"

  id_categoria = Column(Integer, primary_key=True, autoincrement=True)
  nombre_categoria = Column(String(100), nullable=False)
  descripcion = Column(Text)
  edad_recomendada = Column(String(50))
  es_electrico = Column(Boolean, default=False)

  juguetes = relationship("Juguete", back_populates="categoria")
