#Ejercicio 1
"""numero = int(input("Ingresar un numero para saber si es positivo o negativo: "))
if numero > 0:
    print ("El numero ingresado es positivo.")
else:
    print ("El numero ingresado es negativo.")"""

#Ejercicio 2
"""numero = int(input("Ingresar un numero: "))
numero2 = int(input("Ingresar el siguiente numero: "))
if numero > numero2:
    print ("El primer numero ingresado es mayor.")
else:
    print ("El segundo numero ingresado es mayor.")"""

#Ejercicio 3
"""numero = int(input("Ingresar un numero: "))
numero2 = int(input("Ingresar el siguiente numero: "))
if numero == numero2:
    print ("Ambos numeros son iguales.")
else:
    print ("Los numeros son diferentes.")"""

#Ejercicio 4
"""caracter = input("Ingresar una letra aleatoria: "))
caracter2 = input("Ingresar la siguiente letra: "))
if caracter == caracter2:
    print ("Ambas letras son iguales.")
else:
    print ("Las letras son diferentes.")"""

#Ejercicio 5
"""numero1 = int(input("Ingrese el primer valor: "))
numero2 = int(input("Ingrese el segundo valor: "))
numero3 = int(input("Ingrese el tercer valor: "))
suma = numero1+numero2
if suma > numero3:
    print ("La suma de los primeros dos numeros es mayor.")
else:
    print ("El tercer valor ingresado es mayor.")"""

#Ejercicio 6
"""numero1 = int(input("Ingresa el primer valor: "))
if numero1%2==0:
    print ("El numero ingresado es par.")
else:
    print ("El numero ingresado es impar.")"""

#Ejercicio 7
"""numero1 = int(input("Ingrese el primer valor: "))
numero2 = int(input("Ingrese el segundo valor: "))
if numero1%numero2==0:
    print ("El segundo numero es multiplo del segundo")
else:
    print ("El segundo numero NO es multiplo.")"""

#Ejercicio 8
"""numero = int(input("Ingrese un numero del 1 al 7 para devolver el día correspondiente: "))
if numero==1:
    print ("Hoy es lunes.")
else :
    print ("Hoy es martes")
    if numero==3:
        print ("Hoy es miercoles.")
    else:
        print ("Hoy es jueves")
        if numero==5:
            print ("Hoy es viernes.")
        else:
            print ("Hoy es sabado")
            if numero==7:
                print ("Hoy es domingo.")"""

#Ejercicio 9
"""dia = int(input("Ingrese un numero para identificar el día: "))
mes = int(input("Ingrese un numero para identificar el mes: "))
año = int(input("Ingrese un numero para identificar el año: "))
print ("Dia: "+str(dia))
print ("Mes: "+str(mes))
print ("Año: "+str(año))
if mes==1:
    print +str(dia)+" de enero del "+str(año))
else:
    print +str(dia)+" de febrero del "+str(año))
    if mes==3:
        print +str(dia)+" de marzo del "+str(año))
    else:
        print +str(dia)+" de abril del "+str(año))
        if mes==5:
            print +str(dia)+" de mayo del "+str(año))
        else:
            print +str(dia)+" de junio del "+str(año))
            if mes==7:
                print +str(dia)+" de julio del "+str(año))
            else:
                print +str(dia)+" de agosto del "+str(año))
                if mes==9:
                    print +str(dia)+" de septiembre del "+str(año))
                else:
                    print +str(dia)+" de noviembre del "+str(año))
                    if mes==11:
                        print +str(dia)+" de octubre del "+str(año))
                    else:
                        print +str(dia)+" de diciembre del "+str(año))"""

#Ejercicio 10
"""compra = float(input("Ingrese el valor total de su compra para realizar un descuento del mismo: "))
if compra>=1 and compra<=500:
    print ("El monto total de la compra sin descuento es :" +str(compra))
elif compra>500 and compra<1000:
    print ("El monto total de la compra con un descuento del %5 es :" +str(compra-(compra*0.5)))
elif compra>=1000 and compra<5000:
    print ("El monto total de la compra con un descuento del %10 es :" +str(compra-(compra*0.10)))
elif compra>=5000 and compra<15000:
    print ("El monto total de la compra con un descuento del %15 es :" +str(compra-(compra*0.15)))"""


"""#Ejercicio 11
input1 = int(input("Ingresa el primer valor: "))
input2 = int(input("Ingresa el segundo valor: "))
opciones = input("Ingresar una opcion entre A, B y C para realizar una operación: ")
if opciones == "A" or opciones == "a":
    print ("La suma de ambos valores es "+str(input1+input2))
else:
    if opciones == "B" or opciones == "b":
        print ("La resta de ambos valores es "+str(input1-input2))
    else:
        if opciones == "C" or opciones == "c":
            print ("La multiplicación de ambos valores es " +str(input1*input2))"""