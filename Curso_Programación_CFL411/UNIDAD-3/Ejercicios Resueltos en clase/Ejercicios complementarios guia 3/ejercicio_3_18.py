# Escribir un programa que permita contar cuantas veces se repite un numero en una lista de números enteros.
numero_ingresado = int(input("Ingrese un numero: "))
lista_numeros = [1, 3, 5, 7, 3, 9]
contador_repeticiones = 0 # Creo un contador que se va a incrementar cada vez que numero_ingresado se encuentre en la lista de numeros
for numero in lista_numeros: # Para cada numero en la lista de numeros ejecuto el sig. bloque de codigo
    if numero == numero_ingresado: # Si el numero de la iteracion actual es igual al numero ingresado
        contador_repeticiones += 1 # Incremento el contador de repeticiones
print("El numero", numero_ingresado, "se repite", contador_repeticiones, "veces.") # Muestro el contador de repeticiones luego de finalizar el bucle
