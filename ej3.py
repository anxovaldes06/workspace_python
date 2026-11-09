def mostrar_resultados(numeros, cantNumeros):
    
    suma = sum(numeros)
    
    numero_mayor = max(numeros)
    numero_menor = min(numeros)
    
    for num in numeros :
            if num % 2 == 0:
                numeros_pares.append(num)
            
    numeros_ordenados = sorted(numeros)

    print("Lista de números :", numeros)
    print("Cantidad de números almacenados:", cantNumeros)
    print("Suma de todos los números:", suma)
    print("Número mayor:", numero_mayor)
    print("Número menor:", numero_menor)
    print("Números pares:", numeros_pares)
    print("Lista ordenada de menor a mayor:", numeros_ordenados)


numeros_pares = []
numeros = []
cantNumeros = 0

while True:
    entrada = input("Ingrese un número entero: ")

    if entrada == "salir":
        mostrar_resultados(numeros, cantNumeros)
        break
    
    numero = int(entrada)
    numeros.append(numero)
    cantNumeros += 1