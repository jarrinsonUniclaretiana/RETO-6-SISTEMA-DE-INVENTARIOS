# Integrante A - Cálculo del Punto de Reorden

def calcular_punto_reorden(demanda_diaria: float, tiempo_entrega: float, stock_seguridad: float = 0) -> float:
    rop = (demanda_diaria * tiempo_entrega) + stock_seguridad
    return round(rop, 2)


def main_punto_reorden():
    print("\n" + "="*45)
    print("     PUNTO DE REORDEN (ROP)")
    print("="*45)
    
    try:
        demanda = float(input("Demanda diaria promedio (unidades): "))
        entrega = float(input("Tiempo de entrega (días): "))
        seguridad = float(input("Stock de seguridad (0 si no aplica): "))
        
        rop = calcular_punto_reorden(demanda, entrega, seguridad)
        print(f"\n✅ Punto de Reorden: {rop} unidades")
    except ValueError:
        print(" Error: Ingresa solo números.")