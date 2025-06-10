#Consigna:
#Pedir el ingreso de un valor entero
#Mostrar por pantalla si es menor a cero o mayor a cien
#Caso contrario mostrar el mensaje "No cumple ninguna de las condiciones"

#Ingreso de datos
valor = int(input("Ingrese valor entero: "))
#Si el valor ingresado es mayor a 100, muestro por pantalla que el numero es mayor a 100
if valor > 100:
    print("El numero es mayor a 100")
elif valor < 0: # Si es menor a 0, muestro por pantalla que es menor a 0
    print("El numero es menor a 0")
else:  # Caso contrario muestro mensaje indicando que no cumple con las condiciones anteriores
    print("El numero no coincide con ninguna de las condiciones")



