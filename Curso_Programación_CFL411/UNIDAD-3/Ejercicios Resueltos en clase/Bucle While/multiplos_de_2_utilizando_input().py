#5) resolver el ejercicio anterior solicitando
# al usuario ingresar valor_inicial y valor_final
valor_inicial = int(input("Ingrese el valor inicial : ")) #Ahora el contador sera valor_inicial y sera ingresado por el usuario
valor_final = int(input("Ingrese el valor final: ")) #valor_final es hasta donde vamos a contar
while valor_inicial <= valor_final : # Mientras el contador(valor_inicial) sea menor o igual a valor_final
    if valor_inicial % 2 == 0:
        print("el valor: ", valor_inicial, "es multiplo de 2.") #Muestro el valor del contador(valor_inicial) cuando es multiplo de 2
    valor_inicial += 1 #Incremento el contador(valor_inicial)
else: #Cuando el contador(valor_inicial) es igual valor_inicial finaliza el bucle, entonces se ejecuta el bloque else
    print("finalizo el bucle while")