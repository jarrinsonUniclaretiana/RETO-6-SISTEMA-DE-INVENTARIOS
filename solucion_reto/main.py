# main.py
from punto_reorden import main_punto_reorden

def main():
    print("="*60)
    print("   SISTEMA DE GESTIÓN DE INVENTARIOS - RETO 6")
    print("="*60)
    
    while True:
        print("\n1. Calcular Punto de Reorden (Integrante A)")
        print("2. Calcular EOQ (Pendiente - Integrante B)")
        print("3. Calcular Costo Total (Pendiente - Integrante C)")
        print("4. Salir")
        
        opcion = input("\nSeleccione una opción (1-4): ").strip()
        
        if opcion == "1":
            main_punto_reorden()
        elif opcion in ["2", "3"]:
            print("⚠️ Este módulo aún no está disponible.")
        elif opcion == "4":
            print("\n¡Gracias por usar el sistema!")
            break
        else:
            print("❌ Opción inválida.")
        
        input("\nPresione Enter para continuar...")

if __name__ == "__main__":
    main()