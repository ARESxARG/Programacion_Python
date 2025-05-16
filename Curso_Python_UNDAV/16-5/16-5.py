#Bucle For. Clase 16/5 Asincrónica
"""for i in range (2,20,1):
    print (i)
#Otro ejemplo
frase = "Hola a todos"
for letra in frase : #Tambien si agregamos un "reversed" (funcion reservada de Python) entre "in" y "(frase)" se pondra en reversa
    print (letra)"""

#Ejercicios Teoria For
#Ejercicio 1
"""for numeros in range (1,11):
    print (numeros)"""

#Ejercicio 2
"""for numeros in reversed (range(1,11)):
    print (numeros)"""

#Ejercicio 3
"""acumulador = 0
for numeros in range (1,11):
    numeros = int(input("Ingresa numeros aleatorios: "))
    acumulador += numeros    
print ("La suma total de los numeros en cada iteración es: ",acumulador)"""

#Ejercicio 4
"""for numeros_pares in range (10,50,2):
    print (numeros_pares)"""

#Ejercicio 5
"""for numeros_multiplos in range (1,31):
    if (numeros_multiplos % 3) == 0:
        print (numeros_multiplos)"""

#Ejercicio 6
"""acumulador = 0
for iterador in range (1,101):
    if (iterador % 2) != 0:
        acumulador += iterador
print (acumulador)"""

#Ejercicio 7
"""numero_1 = int(input("Ingresa el primer numero: "))
numero_2 = int(input("Ingresa el segundo numero: "))
suma = numero_2+1
for iterador in range(numero_1,suma):
    print (iterador)"""


#Ejercicio 8
"""for iterador in range (1,11):
    numeros = int(input("Ingresa numeros aleatorios para destacar cual es el menor y el mayor: "))
    print (acumulador)"""