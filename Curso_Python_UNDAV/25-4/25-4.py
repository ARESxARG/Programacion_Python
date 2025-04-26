#Operadores lógicos 25/4
"""AND = Y
   OR  = O"""

#Ejemplo del ejercicio 11 utilizando operadores lógicos.
input1 = int(input("Ingresa el primer valor: "))
input2 = int(input("Ingresa el segundo valor: "))
opciones = input("Ingresar una opcion entre A,B y C para realizar una operación: ")
if opciones == "A" or opciones == "a" :
    print ("La suma de ambos valores es "+str(input1+input2))
else:
    if opciones == "B" or opciones == "b" :
        print ("La resta de ambos valores es "+str(input1-input2))
    else:
        if opciones == "C" or opciones == "c" :
            print ("La multiplicación de ambos valores es " +str(input1*input2))


#Ejemplo del ejercicio 10 utlizando el operador "and"
compra = float(input("Ingrese el valor total de su compra para realizar un descuento del mismo: "))
if compra>=1 and compra<500:
    print ("El monto total de la compra sin descuento es :" +str(compra))
elif compra>=500 and compra<1000:
    print ("El monto total de la compra con un descuento del %5 es :" +str(compra-(compra*0.5))) #Para cálculos decimales utilizar punto, en vez de coma
elif compra>=1000 and compra<5000:
    print ("El monto total de la compra con un descuento del %10 es :" +str(compra-(compra*0.10)))
elif compra>=5000 and compra<15000:
    print ("El monto total de la compra con un descuento del %15 es :" +str(compra-(compra*0.15)))