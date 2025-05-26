#Ordenamiento por seleccion (selection sort)
lista = [2, 6, 1, 7, 11, 3]
print("Selection Sort - antes:", lista)

# Recorremos la lista entera
for i in range(len(lista)):
    i_valor_minimo = i  # Suponemos que el mínimo es el actual

    # Buscamos el mínimo en el resto de la lista
    for j in range(i + 1, len(lista)):
        if lista[j] < lista[i_valor_minimo]:
            i_valor_minimo = j

    # Intercambiamos el mínimo encontrado con el primer elemento no ordenado
    aux = lista[i]
    lista[i] = lista[i_valor_minimo]
    lista[i_valor_minimo] = aux

print("Selection Sort - despues:", lista)
