#Programa de ingreso de datos y verificación de administrador
"""admin_nombre = "Alejo"
admin_apellido = "Ortiz"
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
if nombre + apellido == admin_nombre + admin_apellido:
    print ("El nombre y apellido coincide con un administrador.")
else:
    print ("El nombre no es un administrador")

#Segundo ejemplo de programa de ingreso de datos y verificación de administrador
admin_nombre = "Alejo"
admin_apellido = "Ortiz"
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
if nombre == admin_nombre:
    if apellido == admin_apellido:
        print ("El nombre y apellido coincide con un administrador.")
else:
        print ("El nombre no es un administrador")"""

#Ejercicio Condicionales (If-Else)
"""primer_valor = int(input("Ingrese el primer valor: "))
segundo_valor = int(input("Ingrese el segundo valor: "))
tercer_valor = int(input("Ingrese el tercer valor: "))

if primer_valor == 2:
    print ("El primer valor ingresado es el correcto")
if segundo_valor == 2:
    print ("El segundo valor ingresado es el correcto")
if tercer_valor == 2:
    print ("El tercer valor ingresado es el correcto")"""

#Segundo Ejemplo anidado utilizando (elif)
"""valor_unico = int(input("Ingrese un valor entre 1 a 3: "))
if valor_unico == 1:
    print ("El valor ingresado es igual a 1")
elif valor_unico == 2:
    print ("El valor ingresado es igual 2")
elif valor_unico == 3:
    print ("El valor ingresado es igual a 3")
else:
    print ("El valor ingresado es distinto")"""

#Operadores Lógicos. Ejemplo de uso de operador "and" se utiliza para ingresar dos valores condiciones en un mismo "if". 
"""valor_1 = int(input("Ingrese el valor 1: "))
valor_2 = int(input("Ingrese el valor 2: "))
if valor_1 == 1 and valor_2 == 2:
    print ("El valor#1 es igual a 1 y el valor#2 es igual a 2")
else:
    print ("El valor no cumple con ninguno de los dos valores")"""

#Ejemplo de uso de operador "or" se utiliza para ingresar dos valores condiciones en un mismo "if" dando a entender entre uno u otro. 
"""valor = int(input("Ingrese un valor aleatorio: "))
if valor == 1 or valor == 2:
    print ("El valor es igual a 1 o 2")
else:
    print ("El valor ingresado no coincide con ninguno de los dos parámetros (1 o 2)")"""

#Ejercicio 1
"""valor = int(input("Ingrese un valor aleatorio: "))
if valor > 100:
    print ("El numero es mayor a 100.")
elif valor < 0:
    print ("El numero es menor a 0.")
else:
    print ("El numero no coincide con ningun parámetro.")
#Ejemplo 2
valor = int(input("Ingrese un valor aleatorio: "))
if valor < O or valor > 100:
    print ("El numero es mayor a 100 o menor a 0.")
else:
    print ("El numero no coincide con ningun parámetro.")
#Ejemplo 3 invirtiendo el if (para tomar en cuenta los valores entre 0 a 100)
valor = int(input("Ingrese un valor aleatorio: "))
if 0 > valor < 100:
    print ("No cumple con ninguna de las condiciones.")
else:
    print ("El numero es menor a 0 o mayor a 100.")"""