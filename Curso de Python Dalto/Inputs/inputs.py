#Inputs
#Pedirle al usuario que ingrese su nombre
"""nombre = input ("Ingrese su nombre por favor: ")

#Mostrar el nombre ingresado por el usuario concatenado con un saludo
#1ra Forma de concatenar
print (f"Hola {nombre}, bienvenido al curso de Python") #Concatenando con "f-string"
#2da Forma de concatenar
print ("Hola "+nombre+", bienvenido al curso de Python")
"""
#Pedirle al usuario que ingrese un número
numero = input ("Ingresa un número por favor: ")
resultado = numero*2
print (f"El resultado es : {resultado}") #El resultado no es el esperado porque el input devuelve un string y no un número. Es decir, simplemente coloca 2 veces el string que ingresó el usuario. Por ejemplo, si el usuario ingresa 5, el resultado será 55, ya que se concatenan los dos strings.

#Por lo tanto, hay que convertirlo a un número aritmético utilizando la función int o float (que ya vimos anteriormente).
resultado1 = int(numero)*2
resultado2 = float(numero)*2
print (f"El resultado es : {resultado2}") #Correjimos el error anterior convirtiendo el string a un número aritmético con ''int'' y ''float''. Ahora, si el usuario ingresa 5, el resultado será 10.