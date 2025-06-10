#Ejemplo de uso de la funcion type()
#El programa muestra el tipo de dato de variable1, variable2 y variable3
#Luego se modifica el valor almacenado en variable3 por la cadena de texto "hola"
variable1 = 1.0
variable2 = False
variable3 = (2 > 1) and (1 == 2) # True and False => False => es de tipo booleano
print("El tipo de dato de variable1 es: ", type(variable1))
print("El tipo de dato de variable2 es: ", type(variable2))
print("El tipo de dato de variable3 es: ", type(variable3))
variable3 = "Hola" # ahora es de tipo str
print("El tipo de dato de variable3 es: ", type(variable3))