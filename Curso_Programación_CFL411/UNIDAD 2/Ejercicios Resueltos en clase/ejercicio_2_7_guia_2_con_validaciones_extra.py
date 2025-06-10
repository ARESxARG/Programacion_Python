#Agregar un mensaje de error 
#1)si la letra ingresada tiene mas de un caracter
#2)si la letra ingresada no esta dentro del abecedario
#Ayuda 1)
#La funcion que cuenta la cantidad de caracteres de una cadena es len()
#Ejemplo: len("hola") => devuelve 4
#Ayuda 2)
# la expresion (letra >= "a" and letra <= "z") 
# da como resultado True si la letra esta dentro del abecedario
# Ejemplo:
# letra = "c"
#(letra >= "a" and letra <= "z") => devuelve True
# letra = "/"
#(letra >= "a" and letra <= "z") => devuelve False

#Resolucion del ejercicio
#Ingreso de datos
letra = input("Ingrese una letra: ")
#Proceso
if len(letra) == 1 : # Si la longitud de los caracteres de letra es igual a 1 la condicion es valida
    if (letra >= "a" and letra <= "z") or (letra >= "A" and letra <= "Z"): # Si letra es mayor a "a" y menor a "z" se encuentra en el abecedario, lo mismo para las mayusculas
        if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u": #Si letra es igual a alguna de las vocales "a","e","i","o" o "u" es  vocal minuscula
            print("La letra es una vocal minuscula.")
        elif letra == "A" or letra == "E" or letra == "I" or letra == "O" or letra == "U": #Si letra es igual a alguna de las vocales "A","E","I","O" o "U" es  vocal mayuscula
            print("La letra es una vocal mayuscula.")
        else: #Como no es una vocal minuscula o mayuscula entonces es una consonante
            print("La letra es una consonante.")
    else: #Como letra no se encuentra en el abecedario entonces muestro un mensaje de error
        print("Error, la letra ingresada debe estar en el abecedario.")
else: #Como letra tiene mas de un caracter entonces muestro un mensaje de error
    print("Error, debe ingresar solo un caracter.")


