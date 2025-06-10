#Crear una lista que almacene 5 números enteros y mostrar por pantalla solo el  mayor 
lista_numeros = [1,555,88,13,555] #creo una lista con numeros enteros al azar
valor_maximo = 0 #Creo una variable donde voy a almacenar el valor maximo
for elemento in lista_numeros: #Para cada elemento en la lista voy a ejecutar el bloque de codigo siguiente.
    if valor_maximo < elemento: #si valor_maximo es menor a elemento
        valor_maximo = elemento #almaceno el nuevo valor maximo (tener en cuenta que lo estoy "actualizando", no lo estoy incrementando porque no es un contador)
print("El valor maximo es:", valor_maximo) #Cuando finaliza el bucle muestro valor_maximo