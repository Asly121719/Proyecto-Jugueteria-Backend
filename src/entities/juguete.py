from src.database import Base
from sqlalchemy import Column, ForeignKey, Integer, Numeric, String, Table
from sqlalchemy.orm import relationship

promocion_juguetes = Table(
    "promocion_juguetes",
    Base.metadata,
    Column(
        "id_promocion",
        Integer,
        ForeignKey("promociones.id_promocion"),
        primary_key=True,
    ),
    Column(
        "id_juguete",
        Integer,
        ForeignKey("juguetes.id_juguete"),
        primary_key=True,
    ),
    extend_existing=True,  # <--- Debe ir aquí, como argumento de Table, fuera de las columnas
)


class Juguete(Base):
  _tablename_ = "juguetes"

  id_juguete = Column(Integer, primary_key=True, autoincrement=True)
  id_categoria = Column(Integer, ForeignKey("categorias.id_categoria"))
  id_proveedor = Column(Integer, ForeignKey("proveedores.id_proveedor"))
  nombre_producto = Column(String(150), nullable=False)
  precio_unitario = Column(Numeric(10, 2), nullable=False)
  detalles = relationship("DetalleVenta", back_populates="juguete")
  categoria = relationship("Categoria", back_populates="juguetes")
  proveedor = relationship("Proveedor", back_populates="juguetes")
  inventarios = relationship("InventarioTienda", back_populates="juguete")
  promociones = relationship(
      "Promocion", secondary=promocion_juguetes, back_populates="juguetes"
  )