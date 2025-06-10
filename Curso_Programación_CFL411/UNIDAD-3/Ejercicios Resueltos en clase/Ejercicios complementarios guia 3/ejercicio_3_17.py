#Crear una lista que almacene 5 números enteros y mostrar por pantalla el número menor.
lista = [7,8,2,6,10]
valor_minimo = lista[0] # suponemos que el primer elemento es el menor
for valor in lista: # Para cada valor en la lista ejecuto el sig. bloque de codigo
    if valor < valor_minimo: # Si el valor de la lista en la iteracion actual es menor al valor minimo almacenado
        valor_minimo = valor # Actualizo el valor_minimo por el valor del elemento de la lista
print("El numero minimo es: ", valor_minimo) # Muestro el valor minimo luego del bucle