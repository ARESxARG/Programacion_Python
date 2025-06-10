#Escribir un programa pida el ingreso de un numero y muestre la tabla de multiplicar de 1 hasta 10 de ese número.
valor = int(input("Ingrese un numero: ")) # Pido el ingreso de un valor entero
contador = 1 #Inicializo el contador en 1
while contador <= 10: # Mientras el contador sea menor o igual que 10 
    print(valor, "*", contador, "es igual a: ", valor * contador) #Muestro el resultado de la multiplicacion
    contador = contador + 1 #Incremento el contador 