#Condicionales
"""edad = int(input("Ingrese edad: ")) #Indicamos ingresar una variable de numero entero
if (edad>=18):
    print ("Sos mayor")
else :
    print ("Sos menor")"""
#Para indicar si una variable es distinta utilizamos "! y =" (!=)
#Para indicar si las variables son iguales utilizamos dos signos iguales unidos "=="


#Ejercicio1 : Ingresar un numero y mostrar si es positivo o negativo.
numero = int(input("Ingrese un numero: "))
if (numero>=0):
    print ("Ingresaste un numero positivo")
else :
    print("Ingresaste un numero negativo")

#Ejercicio2 : Ingresar dos numeros y mostrar cual de los dos es el mayor.
numero1 = int(input("Ingrese un numero: "))
numero2 = int(input("Ingrese un otro numero: "))
if (numero1>numero2):
    print ("El numero mayor es "+str(numero1))
else :
    print ("El numero es menor"+str(numero2)) 

#Ejercicio3 : Ingresar dos numeros y mostrar si son iguales o no.
numero1 = int(input("Ingrese un numero: "))
numero2 = int(input("Ingrese otro numero: "))
if (numero1==numero2):
    print ("Los numeros son iguales.")
else :
    print ("El numero ingresado es distinto.")

#Ejercicio4 : Ingresar dos caracteres y mostrar si son iguales o no.
primer_caracter = (input("Ingrese una clave alfabética: "))
segundo_caracter = (input("Ingrese nuevamente la clave alfabética: "))
if (primer_caracter==segundo_caracter):
    print ("Clave ingresada correctamente.")
else :
    print ("Las claves no coinciden.")