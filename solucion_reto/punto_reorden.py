# punto_reorden.py
# Integrante A - Calculo del Punto de Reorden

def calcular_punto_reorden(demanda_diaria_promedio: float, tiempo_entrega_dias: float, stock_seguridad: float = 0) -> float:
    """
    Calcula el Punto de Reorden (ROP).
    
    Formula: ROP = (Demanda diaria promedio × Tiempo de entrega) + Stock de seguridad
    
    Args:
        demanda_diaria_promedio (float): Unidades demandadas por dia en promedio
        tiempo_entrega_dias (float): Dias que tarda en llegar el pedido
        stock_seguridad (float): Cantidad extra para evitar faltantes (opcional)
    
    Returns:
        float: Punto de reorden (unidades)
    """
    rop = (demanda_diaria_promedio * tiempo_entrega_dias) + stock_seguridad
    return round(rop, 2)


def solicitar_datos_punto_reorden():
    """Solicita datos al usuario y calcula el punto de reorden."""
    print("\n--- Calculo del Punto de Reorden ---")
    try:
        demanda_diaria = float(input("Ingrese la demanda diaria promedio (unidades): "))
        tiempo_entrega = float(input("Ingrese el tiempo de entrega en dias: "))
        stock_seg = float(input("Ingrese el stock de seguridad (0 si no aplica): "))
        
        rop = calcular_punto_reorden(demanda_diaria, tiempo_entrega, stock_seg)
        print(f"\nEl Punto de Reorden es: {rop} unidades")
        return rop
    except ValueError:
        print("Error: Por favor ingrese numeros validos.")
        return None