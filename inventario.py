import math

def calcular_eoq(demanda, costo_pedido, costo_mantenimiento):
    """
    Calcula la Cantidad Económica de Pedido (EOQ)
    """
    if demanda <= 0 or costo_pedido <= 0 or costo_mantenimiento <= 0:
        return 0  # evitar errores

    eoq = math.sqrt((2 * demanda * costo_pedido) / costo_mantenimiento)
    return eoq