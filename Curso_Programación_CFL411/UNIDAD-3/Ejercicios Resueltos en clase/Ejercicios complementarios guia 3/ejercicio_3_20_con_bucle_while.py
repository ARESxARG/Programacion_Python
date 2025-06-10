# Crear una lista que almacene 5 números enteros 
# y escribir un programa que cree una lista nueva pero ordenados de forma invertida.
lista_numeros = [1, 2, 3, 4, 5]
lista_invertida = []
indice = len(lista_numeros) -1 
while indice >= 0:
    lista_invertida.append(lista_numeros[indice])
    indice -= 1
print("La lista invertida es:", lista_invertida)
