#Ingreso de datos
valor_entero = input("Ingrese un valor entero: ")
valor1  = 5
valor_entero = int(valor_entero)
#Proceso
if valor_entero < valor1 : # Si valor_entero es menor a valor1
    print("El valor ingresado es menor a valor1.") 
elif valor_entero == valor1: #Sino se cumple lo anterior, evaluo si valor_entero es igual a valor1
    print("El valor ingresado es igual a valor1.")
else: #Si ninguna de las condiciones anteriores se cumplen, entonces valor_entero es mayor a valor1
    print("El valor ingresado es mayor a valor1.")