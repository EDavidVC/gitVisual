def calculadora():
    print("=== Calculadora por consola ===")
    print("Operaciones disponibles: +, -, *, /")
    print("Escribe 'salir' para terminar.\n")

    while True:
        operacion = input("Ingresa la operación (+, -, *, /) o 'salir': ").strip()

        if operacion.lower() == "salir":
            print("¡Hasta luego!")
            break

        if operacion not in ("+", "-", "*", "/"):
            print("Operación no válida. Intenta de nuevo.\n")
            continue

        try:
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
        except ValueError:
            print("Error: debes ingresar números válidos.\n")
            continue

        if operacion == "+":
            resultado = num1 + num2
        elif operacion == "-":
            resultado = num1 - num2
        elif operacion == "*":
            resultado = num1 * num2
        elif operacion == "/":
            if num2 == 0:
                print("Error: no se puede dividir entre cero.\n")
                continue
            resultado = num1 / num2

        print(f"Resultado: {num1} {operacion} {num2} = {resultado}\n")


if __name__ == "__main__":
    calculadora()
