def mostrar_resultados(mayor, menor, suma, contador, suspensos, aprobados):
    print("La nota mayor es:", mayor)
    print("La nota menor es:", menor)
    
    if contador > 0:
        media = suma / contador
        print("La media de las notas es:", media)
    else:
        print("La media de las notas es: 0")
        
    print("El número de suspensos es:", suspensos)
    print("El número de aprobados es:", aprobados)


mayor = None
menor = None
suma = 0
contador = 0
numSuspensos = 0
numAprobados = 0

while True:
    entrada = input("Ingrese una nota entre 0 y 10 ")
    
    if entrada == "salir":
        mostrar_resultados(mayor, menor, suma, contador, numSuspensos, numAprobados)
        break

    nota = int(entrada)
    
    if nota < 0 or nota > 10:
        print("La nota debe estar entre 0 y 10.")
        continue

    if mayor is None or nota > mayor:
        mayor = nota
    if menor is None or nota < menor:
        menor = nota

    suma += nota
    contador += 1

    if nota < 5:
        numSuspensos += 1
    else:
        numAprobados += 1

    print("Nota registrada:", nota)