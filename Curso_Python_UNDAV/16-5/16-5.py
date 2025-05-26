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
"""mayor = None
menor = None
for iterador in range (1,11):
    numeros = int(input("Ingresa numeros de forma aleatoria: "))
    if mayor == None and menor == None:
        menor = numeros
    else:
        mayor = numeros
print ("El numero menor es:",menor)
print ("El numero mayor es:",mayor)"""

#Ejercicio 9
"""palabra = input("Ingrese una palabra: ")
contador=0
for letra in palabra:
    if letra == "a" or letra=="e" or letra=="i" or letra=="o" or letra=="u":
        contador +=1
print(contador)"""

#Ejercicio 10
"""palabra = input("Ingrese una palabra: ")
contador=0
for letra in palabra:
    if letra != "a" and letra != "e" and letra != "i" and letra != "o" and letra != "u":
        contador +=1
print(contador)"""

#Ejercicio 11
"""acumulador = 0
for iterador in range (1,16):
    numeros = int(input("Ingresa numeros aleatorios: "))
    acumulador += numeros    
    resultado = acumulador / 15
print (resultado)"""

#Ejercicio 12
"""



"""

#Ejercicio 13
"""frase_ingresada = input("Ingrese una frase aleatoria: ")
for letra in reversed (frase_ingresada):
    print (letra)"""

frase_ingresada = input("Ingrese una frase aleatoria: ")
palabra = ""
for letra in reversed (frase_ingresada):
    palabra += letra
print (palabra)

#Ejercicio 14
