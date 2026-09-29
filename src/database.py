import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Reemplaza esta URL con tu cadena de conexión real de Neon
DATABASE_URL = "postgresql://neondb_owner:npg_coaWhZu5pN2v@ep-flat-tree-ayw3ktrn-pooler.c-5.us-east-2.aws.neon.tech/neondb?sslmode=require&channel_binding=require"

# Se deja una sola línea con pool_pre_ping para evitar que se cierre la conexión con Neon
engine = create_engine(DATABASE_URL, pool_pre_ping=True, pool_recycle=300)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
