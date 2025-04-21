"""#Estructura para condicionales if-else
# "if" es una palabra reservada que indica que se va a realizar una condición ''Si''
# "else" es una palabra reservada que indica que se va a realizar una condición ''Si no''
if True:
    #acción si la condición es cierta
else False:
    #acción si la condición es falsa
"""
#Ejemplo de uso de if-else
edad = 25
if edad >= 18:
    print("Podes pasar")
    print("Todo lo que escriba aqui se ejecutara si la condicion es verdadera")
    print("Ya que forma parte del bloque if y esta dentro del indentado")
else :
    print("No podes pasar")
    print("Lo mismo que antes, pero si la condicion es falsa xD")

#Ejemplo2
usuario_de_base_de_datos = "Alejo Ortiz"
usuario_ingresado = "Alejo"
if usuario_ingresado == usuario_de_base_de_datos:
    print("Bienvenido Alejo Ortiz")
else:
    print("Usuario no encontrado")
    print("Lo siento, no podemos permitirte el ingreso")
#Ejemplo3
