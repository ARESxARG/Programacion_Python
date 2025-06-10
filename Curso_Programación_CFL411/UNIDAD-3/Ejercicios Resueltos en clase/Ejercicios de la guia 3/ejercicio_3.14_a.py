#Crear una lista que almacene 5 números enteros y mostrar por pantalla solo los números pares
lista_numeros = [1,5,8,13,34] #creo una lista con numero enteros al azar
for elemento in lista_numeros: #Para cada elemento en la lista voy a ejecutar el bloque de codigo siguiente.
    if elemento % 2 == 0: #Si el resto de 2 del elemento es igual a 0 entonces es numero par
        print("El elemento: ", elemento, "es par.") #Muestro que el elemento es par