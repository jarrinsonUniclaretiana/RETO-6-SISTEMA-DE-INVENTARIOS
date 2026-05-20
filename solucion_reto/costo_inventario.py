# costo_inventario.py
# Integrante C - Costo Total Anual de Mantener Inventario

def calcular_costo_total_anual(demanda_anual: float, cantidad_pedido: float, 
                               costo_pedido: float, costo_mantenimiento_unitario: float) -> dict:
    """
    Calcula el costo total anual de inventario.
    """
    if cantidad_pedido <= 0:
        raise ValueError("La cantidad de pedido debe ser mayor a cero.")
    
    costo_pedidos_anual = (demanda_anual / cantidad_pedido) * costo_pedido
    costo_mantenimiento_anual = (cantidad_pedido / 2) * costo_mantenimiento_unitario
    costo_total = costo_pedidos_anual + costo_mantenimiento_anual
    
    return {
        "costo_pedidos_anual": round(costo_pedidos_anual, 2),
        "costo_mantenimiento_anual": round(costo_mantenimiento_anual, 2),
        "costo_total_anual": round(costo_total, 2)
    }


def solicitar_datos_costo():
    """Solicita datos y calcula el costo total anual."""
    print("\n--- Costo Total Anual de Inventario ---")
    try:
        demanda = float(input("Ingrese la demanda anual (unidades): "))
        cantidad_pedido = float(input("Ingrese la cantidad por pedido (Q): "))
        costo_pedido = float(input("Ingrese el costo por pedido ($): "))
        costo_mant = float(input("Ingrese el costo de mantenimiento por unidad/año ($): "))
        
        costos = calcular_costo_total_anual(demanda, cantidad_pedido, costo_pedido, costo_mant)
        
        print("\nResultados:")
        print(f"Costo de pedidos anual     : ${costos['costo_pedidos_anual']}")
        print(f"Costo de mantenimiento anual: ${costos['costo_mantenimiento_anual']}")
        print(f"Costo Total Anual           : ${costos['costo_total_anual']}")
        
        return costos
    except ValueError as e:
        print(f"Error: {e}")
        return None