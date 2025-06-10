#Escribir un programa que modifique recorra una lista y si el numero es negativo 
#debe modificarlo por el mismo valor, pero positivo.
lista_de_numeros = [-2,-4,-55,-13,-11] #creo una lista con numeros enteros al azar
print("lista antes:", lista_de_numeros) # Muestro la lista antes de modificarla
indice = 0 #Creo una variable donde voy a almacenar el indice
for elemento in lista_de_numeros: #Para cada elemento en la lista voy a ejecutar el bloque de codigo siguiente.
    if elemento < 0: #Si el elemento es menor a cero
        lista_de_numeros[indice] = elemento * -1 # Modifico su valor convirtiendolo en positivo, si multiplico un nro. negativo por otro negativo el resultado es un nro. positivo.
    indice = indice + 1 #Incremento el valor del indice
print("lista despues: ",lista_de_numeros) # Muestro la lista despues de modificarla

