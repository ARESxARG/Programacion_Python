"""
SIMULACRO PARCIAL
"""

"""
RESPUESTA 1
"""
    #C

"""
RESPUESTA 2
"""
    #A

"""
RESPUESTA 3
"""
    #A) B
    #B) C
    #C) D

"""
RESPUESTA 4
"""
#Escribir un programa que pida el ingreso de dos números positivos y calcule el promedio Requisitos que debe cumplir el programa: 
# • Debe solicitar el ingreso de dos números positivos. 
# • Si el numero ingresado es negativo, debe indicar un error y volver a solicitarlo hasta que el número ingresado sea positivo. 
# • Calcular el promedio de los dos números ingresados y mostrarlo por pantalla.
numero1 = int(input("Ingrese el primer valor: "))
while numero1 < 0:
    numero1 = int(input("El valor ingresado es incorrecto. Ingrese el primer valor nuevamente: "))
numero2 = int(input("Ingrese el primer valor: "))
while numero2 < 0:
    numero2 = int(input("El valor ingresado es incorrecto. Ingrese el segundo valor nuevamente: "))
promedio = (numero1 + numero2) / 2
print("El promedio de los dos números es:", promedio)