#Métodos de Cadenas
cadena1 = "Hola Mundo como estas?"
cadena2 = "Bienvenido al curso de Python"

"""resultado = dir(cadena1) # Muestra todos los métodos que tiene la cadena1
#''dir'' que es una función, sirve para ver los métodos que tiene un objeto. Existen métodos para listas, tuplas, diccionarios, etc.
print(resultado) #Nos mostro la infinidad de métodos que tiene la cadena1
# De todas formas no vamos a usar todos los métodos, solo algunos y de la siguiente manera"""

#Estructura de los métodos: dato o variable.nombre_del_método()
resultado = cadena1.upper() # "upper" Convierte la cadena a mayúsculas
resultado2 = cadena1.lower() # "lower" Convierte la cadena a minúsculas
resultado3 = cadena1.capitalize() # "capitalize" Convierte la primera letra de la cadena a mayúscula

resultado4 = cadena1.find("u") # "find" Busca una subcadena dentro de la cadena y devuelve la posición de la primera aparición. Si no se encuentra, devuelve -1.
resultado5 = cadena1.index("o") # "index" Busca una subcadena dentro de la cadena y devuelve la posición de la primera aparición. Si no se encuentra, lanza un error.

resultado6 = cadena1.isnumeric() # "isnumeric" Verifica si la cadena es numérica (solo contiene dígitos). Devuelve True o False.
resultado7 = cadena1.isalpha() # "isalpha" Verifica si la cadena contiene solo letras. Devuelve True o False.
resultado8 = cadena1.isalnum() # "isalnum" Verifica si la cadena contiene solo letras y números. Devuelve True o False.

resultado9 = cadena1.count("o") # "count" Cuenta cuántas veces aparece una subcadena en la cadena
resultado10 = len(cadena1) # "len" Devuelve la cantidad de caracteres de la cadena

resultado11 = cadena1.startswith("Ho") # "startswith" Verifica si la cadena comienza con una caracter. Devuelve True o False.
resultado12 = cadena1.endswith("do") # "endswith" Verifica si la cadena termina con ese caracter. Devuelve True o False.

resultado13 = cadena1.replace("Mundo", "Pete") # "replace" Reemplaza un caracter por otro en la cadena. Devuelve una nueva cadena.
resultado14 = cadena1.split(",") # "split" Divide la cadena en una lista de subcadenas, usando el separador especificado. Si no se especifica, usa espacios en blanco como separador.

print (resultado14)