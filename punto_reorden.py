
# Integrante A: Punto de Reorden

def calcular_punto_reorden(demanda_diaria, tiempo_entrega, stock_seguridad=0):
    """Calcula el Punto de Reorden"""
    punto_reorden = (demanda_diaria * tiempo_entrega) + stock_seguridad
    return round(punto_reorden, 2)


def calcular_stock_seguridad(desviacion, tiempo_entrega, factor=1.65):
    """Calcula el Stock de Seguridad"""
    import math
    stock = factor * desviacion * math.sqrt(tiempo_entrega)
    return round(stock, 2)


# Prueba
if __name__ == "__main__":
    print("Punto de Reorden:", calcular_punto_reorden(50, 7, 25))