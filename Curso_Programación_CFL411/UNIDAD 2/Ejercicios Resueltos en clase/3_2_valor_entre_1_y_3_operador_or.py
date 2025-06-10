#Pido el ingreso de un valor entre 1 y 3 
#y lo convierto a entero con la funcion int()
valor = int(input("Ingrese un valor entre 1 y 3: ")) 

#El valor ingresado es valido si:
#es igual a 1
#es igual a 2
#es igual a 3
#Caso contrario mostrar mensaje de error
if valor == 1 or valor == 2 or valor == 3:
    print("El  valor ingresado es valido, valor ingresado: ", valor)
else:
    print("El valor ingresado es incorrecto, valor ingresado: ", valor)
