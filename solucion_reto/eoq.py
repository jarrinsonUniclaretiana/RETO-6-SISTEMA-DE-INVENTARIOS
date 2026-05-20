# eoq.py
# Integrante B - Calculo de la Cantidad Economica de Pedido (EOQ)

import math

def calcular_eoq(demanda_anual: float, costo_pedido: float, costo_mantenimiento_unitario: float) -> float:
    """
    Calcula la Cantidad Economica de Pedido (EOQ).
    
    Formula: EOQ = sqrt(2 × D × S / H)
    
    Args:
        demanda_anual (float): Demanda anual en unidades
        costo_pedido (float): Costo por realizar un pedido
        costo_mantenimiento_unitario (float): Costo de mantener una unidad al año
    
    Returns:
        float: Cantidad economica de pedido
    """
    if costo_mantenimiento_unitario <= 0:
        raise ValueError("El costo de mantenimiento debe ser mayor a cero.")
    
    eoq = math.sqrt((2 * demanda_anual * costo_pedido) / costo_mantenimiento_unitario)
    return round(eoq, 2)


def solicitar_datos_eoq():
    """Solicita datos al usuario y calcula el EOQ."""
    print("\n--- Calculo del EOQ (Cantidad Economica de Pedido) ---")
    try:
        demanda_anual = float(input("Ingrese la demanda anual (unidades): "))
        costo_pedido = float(input("Ingrese el costo por pedido ($): "))
        costo_mant = float(input("Ingrese el costo de mantenimiento por unidad al año ($): "))
        
        eoq = calcular_eoq(demanda_anual, costo_pedido, costo_mant)
        print(f"\nLa Cantidad Economica de Pedido (EOQ) es: {eoq} unidades")
        return eoq
    except ValueError as e:
        print(f"Error: {e}")
        return None