# main.py
# Sistema Integrado de Inventarios

from punto_reorden import solicitar_datos_punto_reorden
from eoq import solicitar_datos_eoq
from costo_inventario import solicitar_datos_costo


def main():
    print("=" * 60)
    print("SISTEMA DE GESTION DE INVENTARIOS")
    print("=" * 60)
    
    while True:
        print("\nMenu Principal:")
        print("1. Calcular Punto de Reorden")
        print("2. Calcular EOQ (Cantidad Economica de Pedido)")
        print("3. Calcular Costo Total Anual de Inventario")
        print("4. Salir")
        
        opcion = input("\nSeleccione una opcion (1-4): ").strip()
        
        if opcion == "1":
            solicitar_datos_punto_reorden()
        elif opcion == "2":
            solicitar_datos_eoq()
        elif opcion == "3":
            solicitar_datos_costo()
        elif opcion == "4":
            print("\nGracias por usar el Sistema de Inventarios!")
            break
        else:
            print("Opcion invalida. Intente de nuevo.")
        
        input("\nPresione Enter para continuar...")


if __name__ == "__main__":
    main()