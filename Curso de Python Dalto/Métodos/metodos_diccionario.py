#Creando un diccionario y sus diferentes metodos
diccionario = {
    "nombre": "Alejo",
    "apellido": "Ortiz",
    "edad": 20,
    "estudiante": True
}
claves = diccionario.keys() # ''.keys'' Devuelve las variables o datos del diccionario.
claves1 = diccionario.get("nombre") # ''.get'' Devuelve el valor de la variable "nombre"
diccionario_iterable = diccionario.items() # ''.items'' Devuelve un iterable de tuplas, donde cada tupla contiene una clave y su valor correspondiente.

#diccionario.pop("nombre") # ''.pop'' Elimina el elemento del diccionario, en este caso la variable "nombre"
#diccionario.clear() # ''.clear'' Elimina todos los elementos del diccionario, quedando vacio.
print (diccionario_iterable)
print (diccionario)


"""#Segundo ejemplo de diccionario, aunque no es la mejor forma de hacerlo, se puede crear un diccionario con indices numericos, como si fuera una lista.
diccionario1 = {
    0 : "Alejo",
    1 : "Ortiz",
    2 : 20,
    3 : "estudiante"
}
claves2 = diccionario1[2] #Al colocar la variable entre corchetes se obtiene el valor según el indice de nuestro diccionario en formato lista
print(claves2)""" 