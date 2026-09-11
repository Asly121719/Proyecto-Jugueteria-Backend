from src.database import Base
from sqlalchemy import Column, Integer, Numeric, String, Text
from sqlalchemy.orm import relationship


class Cargo(Base):
  _tablename_ = "cargos"

  id_cargo = Column(Integer, primary_key=True, autoincrement=True)
  titulo_cargo = Column(String(100), nullable=False)
  salario_base = Column(Numeric(10, 2), nullable=False)
  nivel_acceso = Column(String(50), nullable=False)
  funciones_principales = Column(Text, nullable=False)

  empleados = relationship("Empleado", back_populates="cargo")