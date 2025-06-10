#Ingreso/entrada de datos
valor_entero = int(input("Ingresar un numero aleatorio: "))

#Proceso
if valor_entero != 0: # Comparo si valor_entero es disntinto de cero
    if valor_entero < 0 : # Comparo si valor_entero es negativo
        print("El valor es negativo.") # Muestro por pantalla si es negativo
    else:
        print("El valor es positivo.") # Muestro por pantalla si no es negativo
    if valor_entero >= -9 and valor_entero <= 9 : # Verifico si tiene un solo digito
        print("El valor tiene un solo digito") # Muestro por pantalla si tiene un solo digito
    else:
        print("El valor tiene mas de un digito") # Muestro por pantalla que no tiene un solo digito
    if valor_entero % 2 == 0: # Verifico si es multiplo de dos
        print("El valor es multiplo de 2") # Muestro por pantalla si es multiplo de 2
    else:
        print("El valor no es multiplo de 2") # Muestro por pantalla si no es multiplo de 2
else:
    print("Error, el valor ingresado no debe ser cero.") # Muestro por pantalla que el valor ingresado no puede ser cero



