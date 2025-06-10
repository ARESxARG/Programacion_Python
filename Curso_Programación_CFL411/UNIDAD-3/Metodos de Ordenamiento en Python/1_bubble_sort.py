lista = [2, 6, 1, 7, 11, 3]
intercambio = True
print("Bubble Sort - antes:", lista)

# Mientras haya intercambios, seguimos iterando
while intercambio:
    intercambio = False
    for i in range(len(lista) - 1):
        # Si el elemento actual es mayor que el siguiente, los intercambiamos
        if lista[i] > lista[i + 1]:
            aux = lista[i]
            lista[i] = lista[i + 1]
            lista[i + 1] = aux
            intercambio = True  # Hubo un intercambio, hay que seguir

print("Bubble Sort - despues:", lista)






        
    

