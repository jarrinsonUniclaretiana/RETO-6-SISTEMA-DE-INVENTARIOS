def costo_mantenimiento_anual(cantidad_promedio, costo_mantenimiento):
    """
    Calcula el costo anual de mantener inventario.
    
    :param cantidad_promedio: Inventario promedio (Q)
    :param costo_mantenimiento: Costo por unidad al año (H)
    :return: Costo total anual
    """
    if cantidad_promedio < 0 or costo_mantenimiento < 0:
        return 0

    return cantidad_promedio * costo_mantenimiento


def costo_desde_eoq(eoq, costo_mantenimiento):
    """
    Calcula el costo usando EOQ (Q/2 * H)
    """
    inventario_promedio = eoq / 2
    return inventario_promedio * costo_mantenimiento