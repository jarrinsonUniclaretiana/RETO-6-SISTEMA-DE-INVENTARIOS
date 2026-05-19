import inventario

# Datos de ejemplo
demanda = 1000          # unidades por año
costo_pedido = 50       # costo por pedido
costo_mantenimiento = 2 # costo por unidad al año

eoq = inventario.calcular_eoq(demanda, costo_pedido, costo_mantenimiento)

print("Cantidad Económica de Pedido (EOQ):", round(eoq, 2))
