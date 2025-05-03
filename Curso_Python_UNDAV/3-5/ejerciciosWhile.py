"""
#Ejercicio 1
numeros = int(input("Ingresa números aleatorios y para finalizar ingresa el valor 0: "))
while numeros != 0: # "Mientras" = while. Mientras que el numero sea diferente a 0 se va a ejecutar infinitas veces. 
    print ("Ingresaste el numero",numeros)
    numeros = int(input("Ingrese otro numero o 0 para salir: "))
print ("Fin del programa.") #Con este print final, indexado al while, finalizara el programa.
"""

"""#Ejercicio 2
numero = int(input("Ingresa un numero postivo para continuar: "))
while numero >= 0: 
    if numero >= 1:
        print ("Ingresaste un numero positivo:",numero)
        numero = int(input("Ingrese otro numero positivo o 0 para salir: "))
    elif numero == 0:
        print ("Ingresaste el valor 0")
        numero = int(input("Ingrese otro numero positivo o 0 para salir: "))
print ("Ingresaste un valor negativo:",numero)"""

#Ejercicio 3
"""caracter = input("Ingresa caracteres de forma aleatoria. Para finalizar ingrese el valor 0: ")
conteo_palabras = 0
while caracter != "0": 
    conteo_palabras = (conteo_palabras)+1
    print ("Ingresaste:",caracter)
    caracter = input("\nIngresa caracteres aleatorios: ")
print ("La cantidad de caracteres totales es de:",conteo_palabras)"""
#Aclarar en este ejercicio el valor 0 como str dentro del while ("0") para evitar confusiones y errores ya que lo reconoce como entero. Ademas, siempre aclarar un input dentro del while para que no se imprima initinitas veces en la consola.

#Ejercicio 4
"""numero = int(input("Ingrese numeros positivos o negativos. Para finalizar el programa utilice el valor 0: "))
conteo_positivos = 0
conteo_negativos = 0
while numero != 0:
    if numero > 0:
        print ("El numero ingresado es positivo:",numero)
        conteo_positivos = (conteo_positivos)+1
        numero = int(input("\nIngrese otro numero: "))
    elif numero < 0:
        print ("El numero ingresado es negativo:",numero)
        conteo_negativos = (conteo_negativos)+1
        numero = int(input("\nIngrese otro numero: "))
print ("Programa finalizado.""\nCantidad de numeros positivos ingresados:",conteo_positivos,"\nCantidad de numeros negativos ingresados:",conteo_negativos)"""

#Ejercicio 5
"""numero = int(input("Ingrese numeros para determinar si son pares o impares. Para finalizar el programa utilice el valor 0: "))
conteo_pares = 0
conteo_impares = 0
while numero != 0:
    if (numero % 2) == 0:
        print ("El numero ingresado es par:",numero)
        conteo_pares = (conteo_pares)+1
        numero = int(input("\nIngrese otro numero: "))
    elif (numero % 2) != 0:
        print ("El numero ingresado es impar:",numero)
        conteo_impares = (conteo_impares)+1
        numero = int(input("\nIngrese otro numero: "))
print ("Programa finalizado.""\nCantidad de numeros pares ingresados:",conteo_pares,"\nCantidad de numeros impares ingresados:",conteo_impares)"""

#Ejercicio 6
"""while
print"""

#Ejercicio 7
"""letra = input("Ingresa una letra del abecedario: ")
letra2 = input("Ingresa otra letra de abecedario: ")
while letra != letra2:
    letra = input("\nIngrese nuevamente una letra: ")
    letra2 = input("Ingrese nuevamente otra letra: ")
print ("Ingresaste dos letras iguales:",letra,"=",letra2)"""

#Ejercicio 8
numeros = int(input("Ingrese numeros aleatorios: "))
while numeros != 0:
    if numeros >