#Escribir un programa donde se pida al usuario que ingrese un numero
# Si ese numero se encuentra en la matriz
# Mostrar por pantalla en que fila se encuentra el valor ingresado
matriz = [[1,2,3],
          [4,5,6],
          [7,8,9]]

numero_ingresado = int(input("Ingrese un numero: "))

for indice_fila in range(len(matriz)):   # 0 , 1, 2
    for indice_columna in range(len(matriz[indice_fila])): # 0 ,1 , 2
        if matriz[indice_fila][indice_columna] == numero_ingresado:
            print("El numero ingresado se encuentra en la fila:", indice_fila)
        

#for fila in matriz:
#    print(fila)
        
