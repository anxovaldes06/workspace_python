mayor = None

while True:
    numero = input("Ingrese un número: ")

    if numero == "salir":
        print("El número mayor escrito es:", mayor)
        break

    numero = int(numero)

    if mayor is None or numero > mayor:
        mayor = numero

    print("El número ingresado es:", numero)
