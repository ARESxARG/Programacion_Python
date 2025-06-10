#Escribir un programa donde se pida al usuario que ingrese un numero
# Si ese numero se encuentra en la matriz
# Mostrar por pantalla la suma de los valores menores al ingresado
matriz = [[11,2,3],
          [4,5,9],
          [7,8,6]]

numero_ingresado = int(input("Ingrese un numero: "))
acumulador = 0
contador = 0
for indice_fila in range(len(matriz)):   # 0 , 1, 2
    for indice_columna in range(len(matriz[indice_fila])): # 0 ,1 , 2
        if matriz[indice_fila][indice_columna] < numero_ingresado:
            acumulador += matriz[indice_fila][indice_columna]
            contador += 1

print("La suma de los valores menores al ingresado es:", acumulador)
print("La cantidad de elementos menores al ingresado es:", contador)


#for fila in matriz:
#    print(fila)
        
