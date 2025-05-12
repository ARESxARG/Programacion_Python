#Ejercicios 12 de Mayo.
#Ejercicio 3.1 Escribir un programa que muestre los numeros del 1 al 10.
"""contador = 1
while contador <= 5:
    print ("El contador vale:",contador)
    contador +=1
else:
    print ("Fin del programa.")"""

#Ejercicio 3.2. Escribir un programa que sume los numeros del 1 al 5 y muestre el total.
"""contador = 1
acumulador = 0
while contador <= 5:
    print ("El contador vale:",contador)
    acumulador += contador #Cambiar de lugar el acumulador para poder realizar la iteración correctamente.
    contador +=1
else:
    print ("Fin del programa. El contador total vale :",acumulador)"""

#3.3. Escribir un programa que pida el ingreso de un numero y muestre la tabla de multiplicar de 1 hasta 10 de ese numero.

"""contador_para_tabla = 1
numero = int(input("Ingresar un numero para mostrar su tabla de multiplicación: "))
while contador_para_tabla <= 10:
    print (numero,"*",contador_para_tabla,"es igual a:",numero*contador_para_tabla) #Mostrar el numero directamente en el contador para tabla en vez de hacer una variable aparte.
    contador_para_tabla +=1
print ("\nFin del programa.")"""

#3.4. Escribir un programa donde el usuario debe adivinar un numero secreto entre 1 y 10
NUMERO_SECRETO = 7
numero = int(input("¿Cual es mi numero secreto? Ingrese un numero del 1 al 10 para adivinarlo: "))
while numero != NUMERO_SECRETO:
    numero = int(input("Numero secreto incorrecto. Ingrese un valor nuevamente: "))
else:
    print (">>>>> Adivinaste el numero secreto. Recompensa final : FIN DEL BUCLE. <<<<<")