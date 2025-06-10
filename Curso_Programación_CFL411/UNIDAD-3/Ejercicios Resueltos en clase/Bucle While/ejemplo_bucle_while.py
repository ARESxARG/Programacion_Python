contador = 1
acumulador = 0 
while contador <= 5 : # Mientras contador sea menor o igual a 5
    print(contador) #Muestro el valor del contador
    acumulador += contador #Acumulo el valor del contador de cada iteracion
    contador += 1 #Incremento el contador
else: #Cuando contador es igual 6 finaliza el bucle, entonces se ejecuta el bloque else
    print("La suma de todos los valores es:", acumulador)
print("finalizo el bucle")