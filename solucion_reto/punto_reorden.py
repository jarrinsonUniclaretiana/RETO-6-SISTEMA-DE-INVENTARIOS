# Integrante A - Cálculo del Punto de Reorden

def calcular_punto_reorden(demanda_diaria: float, tiempo_entrega: float, stock_seguridad: float = 0) -> float:
    """
    Calcula el Punto de Reorden (ROP).
    
    Parámetros:
        demanda_diaria: unidades por día
        tiempo_entrega: días que tarda en llegar el pedido
        stock_seguridad: unidades de seguridad (opcional)
    
    Retorna: Punto de Reorden
    """
    rop = (demanda_diaria * tiempo_entrega) + stock_seguridad
    return round(rop, 2)


def main_punto_reorden():
    print("=== CÁLCULO DEL PUNTO DE REORDEN ===\n")
    demanda = float(input("Demanda diaria promedio (unidades): "))
    entrega = float(input("Tiempo de entrega (días): "))
    seguridad = float(input("Stock de seguridad (0 si no aplica): "))
    
    rop = calcular_punto_reorden(demanda, entrega, seguridad)
    print(f"\n Punto de Reorden: {rop} unidades")
    print("   (Cuando el inventario llegue a esta cantidad, se debe pedir más)")