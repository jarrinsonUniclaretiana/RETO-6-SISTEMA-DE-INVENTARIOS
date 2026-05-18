# Archivo principal del Sistema de Inventarios

from punto_reorden import main_punto_reorden
from eoq import main_eoq
from costo_inventario import main_costo_inventario

def main():
    print("="*50)
    print("   SISTEMA DE GESTIÓN DE INVENTARIOS")
    print("="*50)
    
    while True:
        print("\nMenú Principal:")
        print("1. Calcular Punto de Reorden")
        print("2. Calcular EOQ (Cantidad Económica de Pedido)")
        print("3. Calcular Costo Total Anual")
        print("4. Salir")
        
        opcion = input("\nSeleccione una opción (1-4): ")
        
        if opcion == "1":
            main_punto_reorden()
        elif opcion == "2":
            main_eoq()
        elif opcion == "3":
            main_costo_inventario()
        elif opcion == "4":
            print("¡Gracias por usar el Sistema de Inventarios!")
            break
        else:
            print("Opción inválida. Intente de nuevo.")
        
        input("\nPresione Enter para continuar...")

if __name__ == "__main__":
    main()