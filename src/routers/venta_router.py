from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from uuid import UUID
from datetime import datetime

from src.database import get_db
from src.entities.venta import Venta
from src.entities.detalle_venta import DetalleVenta
from src.entities.juguete import Juguete
from src.schemas.venta_schema import (
    VentaCreate,
    VentaResponse,
)
from src.utils.constants import (
    HTTP_CREATED,
    HTTP_NOT_FOUND,
    HTTP_OK,
)

router = APIRouter(prefix="/ventas", tags=["Ventas"])

@router.get("/", response_model=List[VentaResponse], status_code=HTTP_OK)
def obtener_ventas(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(Venta).offset(skip).limit(limit).all()

@router.post("/", response_model=VentaResponse, status_code=HTTP_CREATED)
def crear_venta(data: VentaCreate, db: Session = Depends(get_db)):
    total_calculado = 0.0
    detalles_para_guardar = []

    for item in data.detalles:
        juguete = db.query(Juguete).filter(Juguete.id_juguete == item.id_juguete).first()
        if not juguete:
            raise HTTPException(
                status_code=HTTP_NOT_FOUND, 
                detail=f"Juguete con ID {item.id_juguete} no encontrado"
            )
        
        subtotal = float(juguete.precio_unitario) * item.cantidad_comprada
        total_calculado += subtotal

        detalles_para_guardar.append({
            "id_juguete": item.id_juguete,
            "cantidad_comprada": item.cantidad_comprada,
            "subtotal": subtotal
        })

    nueva_venta = Venta(
        id_tienda=data.id_tienda,
        id_empleado=data.id_empleado,
        id_cliente=data.id_cliente,
        fecha_hora_venta=data.fecha_hora_venta or datetime.utcnow(),
        total=total_calculado
    )
    db.add(nueva_venta)
    db.flush()

    for det in detalles_para_guardar:
        nuevo_detalle = DetalleVenta(
            id_venta=nueva_venta.id_venta,
            id_juguete=det["id_juguete"],
            cantidad_comprada=det["cantidad_comprada"],
            subtotal=det["subtotal"]
        )
        db.add(nuevo_detalle)

    db.commit()
    db.refresh(nueva_venta)
    return nueva_venta

@router.get("/{id_venta}", response_model=VentaResponse, status_code=HTTP_OK)
def obtener_venta_por_id(id_venta: UUID, db: Session = Depends(get_db)):
    venta = db.query(Venta).filter(Venta.id_venta == id_venta).first()
    if not venta:
        raise HTTPException(
            status_code=HTTP_NOT_FOUND,
            detail=f"Venta con ID {id_venta} no encontrada"
        )
    return venta

@router.put("/{id_venta}", response_model=VentaResponse, status_code=HTTP_OK)
def actualizar_venta(id_venta: UUID, data: VentaCreate, db: Session = Depends(get_db)):
    venta_existente = db.query(Venta).filter(Venta.id_venta == id_venta).first()
    if not venta_existente:
        raise HTTPException(
            status_code=HTTP_NOT_FOUND,
            detail=f"Venta con ID {id_venta} no encontrada"
        )

    total_calculado = 0.0
    detalles_para_guardar = []

    for item in data.detalles:
        juguete = db.query(Juguete).filter(Juguete.id_juguete == item.id_juguete).first()
        if not juguete:
            raise HTTPException(
                status_code=HTTP_NOT_FOUND, 
                detail=f"Juguete con ID {item.id_juguete} no encontrado"
            )
        
        subtotal = float(juguete.precio_unitario) * item.cantidad_comprada
        total_calculado += subtotal

        detalles_para_guardar.append({
            "id_juguete": item.id_juguete,
            "cantidad_comprada": item.cantidad_comprada,
            "subtotal": subtotal
        })

    venta_existente.id_tienda = data.id_tienda
    venta_existente.id_empleado = data.id_empleado
    venta_existente.id_cliente = data.id_cliente
    if data.fecha_hora_venta:
        venta_existente.fecha_hora_venta = data.fecha_hora_venta
    venta_existente.total = total_calculado

    db.query(DetalleVenta).filter(DetalleVenta.id_venta == id_venta).delete()
    for det in detalles_para_guardar:
        nuevo_detalle = DetalleVenta(
            id_venta=id_venta,
            id_juguete=det["id_juguete"],
            cantidad_comprada=det["cantidad_comprada"],
            subtotal=det["subtotal"]
        )
        db.add(nuevo_detalle)

    db.commit()
    db.refresh(venta_existente)
    return venta_existente

@router.delete("/{id_venta}", status_code=HTTP_OK)
def eliminar_venta(id_venta: UUID, db: Session = Depends(get_db)):
    venta_existente = db.query(Venta).filter(Venta.id_venta == id_venta).first()
    if not venta_existente:
        raise HTTPException(
            status_code=HTTP_NOT_FOUND,
            detail=f"Venta con ID {id_venta} no encontrada"
        )

    db.query(DetalleVenta).filter(DetalleVenta.id_venta == id_venta).delete()
    db.delete(venta_existente)
    db.commit()
    
    return {"mensaje": f"Venta con ID {id_venta} eliminada con éxito"}