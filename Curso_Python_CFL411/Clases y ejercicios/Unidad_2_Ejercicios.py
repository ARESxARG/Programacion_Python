#Unidad 2 - Tipo de dato Booleano - Operadores relacionales - Estructuras 
#Condicionales- Operadores Lógicos

#Ejercicio 2.1
"""activo = True
inactivo = False
print (activo)
print (inactivo)"""

#Ejercicio 2.2
"""altura_maxima = int(200)
nueva_altura = int(input("Ingrese una altura: "))
resultado = nueva_altura > altura_maxima #Declarar una variable para demostrar un valor booleano utilizando los operadores de comparación
print ("¿La nueva altura ingresada supera la altura máxima(200)?" ,resultado)"""
#Otra Manera de realizar el ejercicio
"""altura_maxima = int(200)
nueva_altura = int(input("Ingrese una altura en numeros enteros: "))
print ("¿La nueva altura ingresada supera la altura máxima(200)?" ,nueva_altura > altura_maxima)"""

#Ejercicio 2.3
"""valor = int(5)
valor_aleatorio = int(input("Ingrese un valor entero aleatorio: "))
print ("El valor ingresado es menor a 5" ,str(valor_aleatorio < valor))
print ("El valor ingresado es igual a 5" ,str(valor_aleatorio == valor))
print ("El valor ingresado es mayor a 5" ,str(valor_aleatorio > valor))"""

#Ejercicio 2.4
"""altura_maxima = int(200)
nueva_altura = int(input("Ingrese una altura con numeros enteros: "))
if nueva_altura > 200:
    print ("La nueva altura es mayor o igual(200) a la altura máxima")
else:
    print ("La nueva altura es menor a la altura máxima")"""

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
if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u" and letra == str:
    print ("La letra es una vocal")
else:
    print ("La letra es una consonante o no es un caracter alfabético.")"""

#Ejercicio 2.8
"""valor_entero = int(input("Ingresar un número aleatorio:"))
if valor_entero == 0:
    print ("////////// ERROR 404 NOT FOUND //////////") #OTRA FORMA DE ANIDAR IF/ELSE SEGUN CONSIGNA.
else: #Validacioes de numero
    if valor_entero >= 1:
        print ("El número es positivo.")
    if valor_entero <= -1:
        print ("El número es negativo")
    if (valor_entero % 2) == 0:
        print ("El número es múltiplo de 2.")
    if -9 <= valor_entero <= 9:
        print ("El numero posee un solo dígito.")"""
#Otra Manera de resolverlo
"""if valor_entero != 0:
    if valor_entero > 0:
        print ("El número es positivo.")
    else:
        print ("El número es negativo")
    if (valor_entero % 2) == 0:
        print ("El número es múltiplo de 2.")
    if -9 <= valor_entero <= 9:
        print ("El numero posee un solo dígito.")
else:
    print ("////////// ERROR 404 NOT FOUND //////////")"""
#En caso de que ingresen un string.
"""valor_string = input("Ingresar un numero aleatorio: ")
if valor_string >= "0" and valor_string <= "9":
    valor_entero = int(valor_string)
    if valor_entero != 0:
        if valor_entero > 0:
            print ("El número es positivo.")
        else:
            print ("El número es negativo")
        if (valor_entero % 2) == 0:
            print ("El número es múltiplo de 2.")
        if -9 <= valor_entero <= 9:
            print ("El numero posee un solo dígito.")
    else:
        print ("////////// ERROR 404 NOT FOUND //////////")
else:
    print ("El valor ingresado es incorrecto.")"""

#Ejercicio 2.9
"""compra_total = float(input("Ingrese la cantidad total de su compra: "))
edad = int(input("Ingrese su edad para verificar si tiene un descuento: "))
descuento1 = "A344B"
descuento2 = "B578F"
codigo_descuento = (input("¿Tenes un codigo de descuento?: "))
if codigo_descuento == descuento1 or codigo_descuento == descuento2:
    print ("El monto total de la compra con el codigo de descuento del %5 es :" +str(compra_total-(compra_total*0.5)))
else:
    if edad < 18:
        print ("Total de la compra con un descuento del %10 para menores es :" +str(compra_total-(compra_total*0.10)))
    elif edad >= 18 and edad < 60:
        print ("Total de la compra con un descuento del %5 para mayores de edad es :" +str(compra_total-(compra_total*0.05)))
    elif edad >= 60:
        print ("Total de la compra con un descuento del %15 para jubilados gaga es :" +str(compra_total-(compra_total*0.15)))"""

#Ejercicio 2.10
plato_A = "opción del plato principal A: Milanesas con papas - $8000"
plato_B = "opción del plato principal B: Pollo al horno con papas - $7000"
plato_C = "opción del plato principal C: Ravioles con salsa blanca - $9000"
total = 0
print ("Bienvenido al sistema. A continuación seleccione su plato principal:\nOpción A: Milanesas con papas - $8000\nOpción B: Pollo al horno con papas - $7000\nOpción C: Ravioles con salsa blanca - $9000")
plato_seleccionado = input("\nIngrese la opción del platillo segun su letra correspondiente: ")
valor_plato_A = int(8000)
valor_plato_B = int(7000)
valor_plato_C = int(9000)
if plato_seleccionado == "A" or plato_seleccionado == "a":
    print ("Seleccionaste la",plato_A)
    total = total + valor_plato_A
elif plato_seleccionado == "B" or plato_seleccionado == "b":
    print ("Seleccionaste la",plato_B)
    total = total + valor_plato_B
elif plato_seleccionado == "C" or plato_seleccionado == "c":
    print ("Seleccionaste la",plato_C)
    total = total + valor_plato_C
else:
    print ("No existe el plato solicitado en la carta.")
#Menu Bebidas
bebida_A = "opción A: Agua Saborizada - $1500"
bebida_B = "opción B: Gaseosa - $2000"
valor_bebida_A = int(1500)
valor_bebida_B = int(2000)
print ("\nSeleccione la bebida que va a consumir: \nOpción A: Agua Saborizada - $1500\nOpción B: Gaseosa - $2000")
bebida_seleccionada = input("Ingrese la opción de la bebida segun su letra correspondiente: ")
if bebida_seleccionada == "A" or bebida_seleccionada == "a":
    print ("Seleccionaste la",bebida_A)
    total = total + valor_bebida_A
elif bebida_seleccionada == "B" or bebida_seleccionada == "b":
    print ("Seleccionaste la",bebida_B)
    total = total + valor_bebida_B
else:
    print ("No existe la bebida solicitada en la carta.")
#Menu Postre
postre_A = "Opción A: Flan con crema - $2500"
postre_B = "Opción B: Helado - $3000"
valor_postre_A = int(2500)
valor_postre_B = int(3000)
print ("\nSeleccione el postre que va a consumir: \nOpción A: Flan con crema - $2500\nOpción B: Helado - $3000")
postre_seleccionado = input("Ingrese la opción del postre segun su letra correspondiente: ")
if postre_seleccionado == "A" or postre_seleccionado == "a":
    print ("Seleccionaste la",postre_A)
    total = total + valor_postre_A
elif postre_seleccionado == "B" or postre_seleccionado == "b":
    print ("Seleccionaste la",postre_B)
    total = total + valor_postre_B
else:
    print ("No existe el postre solicitado en la carta.")
#MONTO TOTAL
print("\nTOTAL A PAGAR: $",total)