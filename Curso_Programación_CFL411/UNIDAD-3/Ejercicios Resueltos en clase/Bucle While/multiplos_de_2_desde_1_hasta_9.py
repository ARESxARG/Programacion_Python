#4) mostrar solo los multiplos de 2 contando desde 1 a 9
contador = 1
while contador <= 9 : # Mientras contador sea menor o igual a 9
    if contador % 2 == 0:
        print("el valor: ", contador, "es multiplo de 2.") #Muestro el valor del contador cuando es multiplo de 2
    contador += 1 #Incremento el contador
else: #Cuando contador es igual 10 finaliza el bucle, entonces se ejecuta el bloque else
    print("finalizo el bucle while")