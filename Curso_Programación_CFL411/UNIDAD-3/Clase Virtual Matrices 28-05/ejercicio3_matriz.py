#Escribir un programa donde se pida al usuario que ingrese un numero
# Si ese numero se encuentra en la matriz
# Mostrar por pantalla cuantas veces se repite ese nro. dentro de la matriz
matriz = [[3,3,3],
          [4,6,6],
          [7,7,9]]

numero_ingresado = int(input("Ingrese un numero: "))
contador_repeticiones = 0

for indice_fila in range(len(matriz)):   # 0 , 1, 2
    for indice_columna in range(len(matriz[indice_fila])): # 0 ,1 , 2
        if matriz[indice_fila][indice_columna] == numero_ingresado:
            contador_repeticiones += 1

print("La cantidad de repeticiones es:", contador_repeticiones)


#for fila in matriz:
#    print(fila)
        
