"""
28/4 - Tipos de datos / variables
variable1 = 1.0
variable2 = False
variable3 = 2 > 1
print ("El tipo de dato de variable1 es: ", type(variable1))
print ("El tipo de dato de variable2 es: ", type(variable2))
print ("El tipo de dato de variable3 es: ", type(variable3))
variable3 = "Hola"
print ("El tipo de dato de variable3 es: ", type(variable3))"""

#Funcion "len" Cuenta la cantidad de caracteres (en este caso la igualamos a 1 caracter). Ejemplo con el ejercicio 7 de la unidad 2:
"""
letra = "/"
print (letra >= "a" and letra <= "z") >>>>>>> esto devuelve "false" ya que analiza el orden alfabetico y si la variable en cuestion corresponde a una letra del abecedario.
"""
"""letra = input("Ingrese una letra: ")

if len(letra) == 1:
    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
        print ("La letra es una vocal")
    else:
        print ("La letra es una consonante")
else:
    print ("Error, debe ingresar solo una letra.")"""


letra = input("Ingrese una letra: ")
if (letra >= "a" and letra <= "z") or (letra >= "A" and letra <= "Z"):
    if letra == "a" or letra == "A" or letra == "e" or letra == "E" or letra == "i" or letra == "I" or letra == "o" or letra == "O" or letra == "u" or letra == "U":
        print ("La letra es una vocal")
    else:
        print ("Es una consonante")
else:
    print ("Ingrese un caracter alfabético.")