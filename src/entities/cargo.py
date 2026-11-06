import uuid
from sqlalchemy import Column, Numeric, String, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from src.database import Base

class Cargo(Base):
    __tablename__ = "cargos"

    id_cargo = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    titulo_cargo = Column(String(100), nullable=False)
    salario_base = Column(Numeric(10, 2), nullable=False)
    nivel_acceso = Column(String(50), nullable=False)
    funciones_principales = Column(Text, nullable=False)

    empleados = relationship("Empleado", back_populates="cargo")