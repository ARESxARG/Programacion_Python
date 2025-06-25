"""
Escribir un programa que pida el ingreso de 5 numeros positivos y muestre por pantalla la suma de los numeros mayores de 5. Requisitos que debe cumplir el programa: 
1_ Debe solicitar el ingreso de 5 numeros positivos
2_ Si el numero ingresado es menor que cero, debe indicar un error y finalizar el programa
3_ Mostrar por pantalla la suma de los numeros mayores de 5.
"""
#Ingreso de Datos
acumulador = 0
for i in range (0,5):
    numero = int(input("Ingrese un valor positivo: "))
    if numero < 0: #Bloque para finalizar el programa en caso de que ingrese 0
        print ("Ingresaste un numero negativo. Fin del programa.")
        break
    if numero > 5: #Suma de valores mayores de 5.
        acumulador += numero
print ("La suma de los numeros mayores a 5 es :",acumulador)