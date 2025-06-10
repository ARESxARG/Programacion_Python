#Crear una lista que almacene 5 números enteros positivos y negativos.
#Escribir un programa que cree una lista nueva con solo números positivos.
#En este ejemplo vamos a utilizar la funcion append()
lista_numeros = [-1, 4, -5, 7, -11, 8] # Creo la lista con los nros. positivos y negativos
lista_positivos = [] # Creo una lista vacia donde voy a guardar los numeros positivos
for numero in lista_numeros: # Para cada numero en la lista de numeros ejecuto el sig. bloque de codigo
    if numero > 0: #Si el numero de la iteracion actual es mayor a cero
        lista_positivos.append(numero) # Lo agrego a la lista de positivos con la funcion .append()
#Cuando finaliza el bucle ya puedo mostrar la lista de positivos
print("La lista de positivos es:", lista_positivos)
