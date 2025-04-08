# Creando una lista con la funcoón "list()". La función list() convierte los caracteres en una lista
lista = list(["Hola", "Alejo", "25"])

resultado = len(lista) # "len()" devuelve la cantidad de caracteres de la lista
lista.append("Soy estudiante") # La función "append()" agrega un elemento al final de la lista

lista.insert(0, "Hola") # "insert()" agrega un elemento en el indice especifico de la lista, en este caso al inicio de la lista

lista.extend(["Python","XD","Java"]) # "extend()" agrega una lista a otra lista

lista.pop(0) # "pop()" elimina un elemento de la lista teniendo en cuenta el índice
lista.pop(-1) # "pop()" elimina el último elemento de la lista. Y asi sucesivamente si vamos aplicando un numero negativo mas grande.

#lista.remove("XD") # "remove()" elimina un elemento de la lista teniendo en cuenta el valor del elemento
#lista.clear() # "clear()" elimina todos los elementos de la lista

lista.sort() # "sort()" ordena la lista de menor a mayor o en este caso de alfabéticamente de A a Z. Y si le agregamos el parámetro "reverse=True" lo invierte, de Z a A.
lista.reverse() # "reverse()" invierte el orden de la lista, de mayor a menor o de Z a A.

print(lista)