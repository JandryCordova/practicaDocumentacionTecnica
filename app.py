def sumar(numero1, numero2):
    return numero1 + numero2

try:
    numero1 = float(input("Ingrese el primer número: "))
    numero2 = float(input("Ingrese el segundo número: "))

    resultado = sumar(numero1, numero2)

    print(f"La suma es: {resultado}")

except ValueError:
    print("Error: Debe ingresar únicamente números.")