#Unidad 1 - Variables-Operadores Aritméticos- Diagrama de Flujo
"""
#Ejercicio 1.1
nombre = "Pedro"
print ("Hola" ,nombre)

#Ejercicio 1.2
num1 = 10
num2 = 10
suma = num1+num2
print ("La suma da un total de ",suma)

#Ejercicio 1.3
nombre = "Pedro"
edad = 22 
print ("El nombre del estudiante es: " + nombre)
print ("La edad del estudiante es: " ,edad) #El error se encuentra en esta linea porque no esta correctamente concatenado. La función se utiliza entre "+" o unicamente con la ","

#Ejercicio 1.4
alfa = 2
beta = 4
gama = alfa + beta
print ("El valor de alfa es: ", alfa)
print ("El valor de beta es: ", beta)
print ("El valor de alfa + beta es: ", gama)
alfa = alfa + 3
gama = alfa+beta
print ("El valor de alfa es: ", alfa)
print ("El valor de beta es: ", beta)
print ("El valor de alfa + beta es: ", gama) #Error de cálculo y aclaración de variables

#Ejercicio 1.5
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
promedio = num1+num2/2
al_cuadrado = num1**2
suma_al_cuadrado = (num1+num2)**2
print ("El promedio de ambos valores es de: ",promedio)
print ("El cuadrado del primer valor es de: ",al_cuadrado)
print ("La suma de ambos valores al cuadrado es de: ",suma_al_cuadrado)

#Ejercicio 1.6
celcius = int(input("Ingrese el valor de una temperatura en grados Celsius(°C) para convertirla en grados Fahrenheit(°F) : "))
conversion = (celcius*9/5)+32
print ("La temperatura convertida en grados Fahrenheit es de" ,conversion)
"""

#Ejercicio 1.7
stock_total = int(input("Ingrese la cantidad de productos en su stock total: "))
sucursales = int(input("Ingrese la cantidad de sucursales existentes: "))
productos = stock_total//sucursales
resto_productos = stock_total%sucursales
print ("La cantidad de productos para cada sucursal es de",productos,"y la cantidad de sobrante de productos es de",resto_productos)
