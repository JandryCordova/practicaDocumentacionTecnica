def sumar(numero1, numero2):
    return numero1 + numero2

def pedir_numero(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("❌ Error: Debe ingresar únicamente números. Intente de nuevo.")

def main():
    print("=== Programa de Suma Mejorado ===")
    while True:
        numero1 = pedir_numero("Ingrese el primer número: ")
        numero2 = pedir_numero("Ingrese el segundo número: ")

        resultado = sumar(numero1, numero2)
        print(f"✅ La suma es: {resultado}")

        opcion = input("¿Desea realizar otra suma? (s/n): ").strip().lower()
        if opcion != "s":
            print("👋 Gracias por usar el programa. ¡Hasta pronto!")
            break

if __name__ == "__main__":
    main()
