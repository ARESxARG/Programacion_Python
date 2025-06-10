# Crear una lista que almacene 5 números enteros 
# y escribir un programa que cree una lista nueva pero ordenados de forma invertida.

lista_numeros = [1, 2, 3, 4, 5]
lista_invertida = [] # Creo una lista vacia donde voy a guardar los numeros invertidos
for indice in range(len(lista_numeros)-1, -1 , -1) : # creo un rango de numeros de 4 hasta -1 => (4,3,2,1,0)
    lista_invertida.append(lista_numeros[indice]) #
print("La lista invertida es:", lista_invertida)