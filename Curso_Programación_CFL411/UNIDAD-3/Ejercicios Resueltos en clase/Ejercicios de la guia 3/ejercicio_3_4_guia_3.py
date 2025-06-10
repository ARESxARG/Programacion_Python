#Escribir un programa donde el usuario debe adivinar un numero secreto entre 1 y 10
numero_secreto = 7 # Inicializo una variable con el nro. secreto
numero = int(input("Cual es el numero secreto? Ingrese un numero del 1 al 10 para adivinarlo: ")) #Pido el ingreso de un numero entero
while numero != numero_secreto: #Mientras el numero ingresado sea distinto que el numero secreto
    #Como el numero ingresado no es el correcto, entonces vuelvo a pedir un numero
    numero = int(input("Cual es el numero secreto? Ingrese un numero del 1 al 10 para adivinarlo: "))
else: #Como el numero ingresado era igual al secreto entonces ejecuto el bloque else
    print("Adivinaste el nro secreto. Fin del bucle.") #Muestro que acerto el nro. secreto