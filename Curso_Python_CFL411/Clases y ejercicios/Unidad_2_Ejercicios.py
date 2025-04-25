"""Unidad 2 - Tipo de dato Booleano - Operadores relacionales - Estructuras 
Condicionales- Operadores Lógicos"""

"""#Ejercicio 2.1
activo = True
inactivo = False
print (activo)
print (inactivo)

#Ejercicio 2.2
altura_maxima = int(200)
nueva_altura = int(input("Ingrese una altura: "))
print ("La nueva altura ingresada supera la altura máxima(200)) nueva_altura > altura_maxima
print ("La nueva altura ingresada no supera la altura máxima(200)) nueva_altura < altura_maxima"""

#Ejercicio 2.3
"""valor = int(5)
valor_aleatorio = int(input("Ingrese un valor entero aleatorio: "))
print ("El valor ingresado es menor a 5" ,str(valor_aleatorio < valor))
print ("El valor ingresado es igual a 5" ,str(valor_aleatorio == valor))
print ("El valor ingresado es mayor a 5" ,str(valor_aleatorio > valor))"""

#Ejercicio 2.4
"""altura_maxima = int(200)
nueva_altura = int(input("Ingrese una altura: "))
if nueva_altura > 200:
    print ("La altura es mayor a la altura máxima")
else:
    print ("La altura es menor(200) a la altura máxima")"""

#Ejercicio 2.5
"""valor = int(5)
valor_aleatorio = int(input("Ingrese un valor entero aleatorio: "))
if valor_aleatorio < valor:
    print ("El valor ingresado es menor a 5")
elif valor_aleatorio == valor:
    print ("El valor es igual a 5")
elif valor_aleatorio > valor:
    print ("El valor es mayor a 5")"""

#Ejercicio 2.6
"""contraseña_valida = "secreta123"
ingresar_contraseña = input("Ingrese su contraseña: ")
if ingresar_contraseña == contraseña_valida:
    print ("Acceso Permitido.")
else:
    print ("Acceso Denegado.")"""

#Ejercicio 2.7
"""letra = input("Ingrese una letra para verificar si es vocal o consonante: ")
if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
    print ("La letra es una vocal")
else:
    print ("La letra es una consonante.")"""

#Ejercicio 2.8
"""valor_entero = int(input("Ingresar un numero aleatorio:"))
if valor_entero > 0:
    print ("El numero es positivo")
elif valor_entero < -0:
    print ("El numero es negativo")
elif valor_entero <= 9:
    print ("El numero posee un solo dígito.")
elif (valor_entero % 2) == 0:
    print ("El numero es múltiplo de 2")
else:
    print ("Error de programación.")"""

#Ejercicio 2.9
descuento18 = "A1"
descuento18a60 = "A2"
descuento60 = "A3"
descuento5 = "A344B" or "B578F"
compra_total = float(input("Ingrese el valor total de su compra: "))
edad = int(input("Ingrese su edad: "))
descuento = str(input("Ingrese un código de descuento: "))
if edad < 18 and descuento == descuento18:
    print ("Tenes un descuento del %10 por ser menor de edad")
elif 60 < edad > 18 and descuento == descuento18a60:
    print ("Tenes un descuento del %5 por ser mayor de edad")
elif edad > 60 and descuento == descuento60:
    print ("Tenes un descuento del %15 por ser menor de edad")
elif descuento == descuento5:
    print ("Tenes un descuento exclusivo")