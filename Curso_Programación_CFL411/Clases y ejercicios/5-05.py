#Ejercicio 2.9 Hecho en clase
"""print ("Bieniveida al sistema de calculo de descuentos")
monto_total = float(input("Ingrese el monto total de la compra: "))
edad = int(input("Ingrese la edad del comprador: "))
codigo_descuento = input("Ingrese el codigo de descuento: ")
descuento_por_edad = 0
if edad < 18:
    descuento_por_edad = monto_total * 0.10
    print ("El descuento por edad es de: ",descuento_por_edad,"$")
elif edad >= 18 and edad <= 60:
    descuento_por_edad = monto_total * 0.05
    print ("El descuento por edad es de: ",descuento_por_edad,"$")
elif edad >= 60:
    descuento_por_edad = monto_total * 0.10
    print ("El descuento por edad es de: ",descuento_por_edad,"$")

if codigo_descuento == "A344B" or codigo_descuento == "B578F":
    descuento_codigo"""

#Ejercicio 2.10 Hecho en clase
"""#Variables Iniciales
monto_total = 0
#Mensaje de Bienvenida
print ("Hola, Bienvenido al Sistema.")
print ("Las opciones de plato principal son: ")
print ("opción  a : Milanesas con papas - $8000")
print ("opción  b : Pollo al horno con papas - $7000")
print ("opción  c : Ravioles con salsa blanca - $9000")
plato_principal = input("Ingrese alguna de las opciones (a) (b) (c): ")
if plato_principal == "a" or plato_principal == "b" or plato_principal == "c":
    if plato_principal == "a":
        monto_total = 8000 #Aca ya tendriamos declarados los montos totales para cada variable.
    elif plato_principal == "b":
        monto_total = 7000
    elif plato_principal == "c":
        monto_total = 9000
else:
    print ("Error, la opción ingresada es incorrecta.")
#Seleccion de la bebida
print ("opción  a : Agua saborizada- $1500") 
print ("opción  b : Gaseosa - $2000")
opcion_bebida = input("Ingrese alguna de las opciones validas (a) (b): ")
if opcion_bebida == "a" or opcion_bebida == "b" or opcion_bebida == "c":
    if opcion_bebida == "a":
        monto_total = monto_total + 1500 #Aca ya tendriamos declarados los montos totales para cada variable.
    elif opcion_bebida == "b":
        monto_total = monto_total + 2000
else:
    print ("Error, la opción ingresada es incorrecta.")
#Aca copio y pego lo mismo pero con las opciones del postre.
print ("El monto total a pagar es de: ",monto_total,"$")"""


#Programa: Ingrese un valor y mostrar los 3 numeros consecutivos.
"""numero = int(input("Ingrese un numero para sumarlo: "))
numero_continuacion_1 = numero +1
numero_continuacion_2 = numero_continuacion_1 + 1
numero_continuacion_3 = numero_continuacion_2 + 1
print ("Los siguientes numeros del valor ingresados son: ")
print (numero_continuacion_1)
print (numero_continuacion_2)
print (numero_continuacion_3)"""

#BUCLE WHILE ¿Como utilizarlo?
#Contar los numeros de 1 a 5
"""valor_inicial = 1
while valor_inicial <= 5: #While lo que hace es imprimir la secuencia debajo, la cantidad de veces que se especifique. En este caso evalua la expresion logica y corta hasta que deje de ser falso (5).
    print(valor_inicial) 
    valor_inicial = valor_inicial + 1 #Para que se actualice al numero siguiente.
print ("Finalizo el bucle ''while''.")"""


#CONSIGNAS 
"""
#1) Modificar el programa para que cuente hasta 10.
#2) Modificar el programa para que empiece a contar desde 5.
#3) Modificar el programa para que muestre de dos en dos.
#4) Mostrar.
"""
"""valor_inicial = 5
while valor_inicial <= 10:
    print(valor_inicial) 
    valor_inicial = valor_inicial + 2 #Para que se actualice al numero siguiente.
print ("Finalizo el bucle ''while''.")"""

valor_inicial = 5
while valor_inicial <= 10:
    print(valor_inicial) 
    valor_inicial = valor_inicial + 2 #Para que se actualice al numero siguiente.
print ("Finalizo el bucle ''while''.")