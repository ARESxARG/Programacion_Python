#Ordenamiento por insercion (insertion sort)
lista = [6, 2, 1, 7, 11, 3]
print("Insertion Sort - antes:", lista)

# Recorremos la lista desde el segundo elemento
for i in range(1, len(lista)):
    actual = lista[i]  # Elemento que queremos insertar en la parte ordenada
    j = i - 1

    # Movemos elementos mayores que 'actual' hacia la derecha
    while j >= 0 and lista[j] > actual: # 
        lista[j + 1] = lista[j]
        j -= 1

    # Insertamos el elemento en la posición correcta
    lista[j + 1] = actual # 

print("Insertion Sort - despues:", lista)
