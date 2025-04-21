"""#Inicio de Algorítmo

#Ejercicio1SumaNormal
print ("Suma de dos valores.")
numero1 = int(input("Ingrese un numero: "))
numero2 = int(input("Ingresa el siguiente número: "))
suma = int(numero1)+int(numero2)
print ("El resultado de la sumatoria es de : " +str(suma))

#Ejercicio2SumatoriaconInput
print ("\nEjercicio 2. Ingresar un numero y figure el siguiente")
numero1 = int(input("Ingrese un numero: "))
suma = (numero1+1)
print ("El siguiente número es: " +str(suma))

#Ejercicio3PerímetroDeUnCuadrado
lado = float(input("\n\nIngrese el valor de un lado del cuadrado: "))
perimetro = lado*4
print ("El perímetro del cuadrado es :" +str(perimetro))

#Ejercicio4
producto = float(input("Ingrese el valor en pesos del producto: "))
cantidad = int(input("¿Cuantas unidades va a llevar del producto? "))
total = producto*cantidad
print ("El monto total me da un valor de: " +str(total))

#Ejercicio5
pesos = float(input("Ingrese la cantidad de pesos a convertir: "))
dolar = int(200)
conversion = pesos/dolar
print ("El valor total en dólares seria de $"+str(conversion))

#Ejercicio6
metros = float(input("Ingrese la cantidad de metros: "))
kilometros = metros/1000
centimetros = metros*100
print ("Conversión en Km: " +str(kilometros))
print ("Conversión en Cm: " +str(centimetros))
"""
#Ejercicio7
producto1 = float(input("Ingrese el valor del primer producto: "))
producto2 = float(input("Ingresa el valor del segundo producto: "))
producto3 = float(input("Ingresa el valor del tecer producto: "))
total = producto1 + producto2 + producto3
IVA = total*1.21
print ("El valor total con IVA del 21% es del : " +str(IVA))
print ("El valor total sin IVA es de : " +str(total))
#Fin de Algorítmo