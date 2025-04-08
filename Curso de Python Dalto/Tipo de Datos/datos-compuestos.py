lista = ["Alejo Ortiz","Soy Alejo",True, 1.68] #Es una matriz de datos compuestos por diferentes tipos de datos. En este caso, una cadena de texto, un booleano y un número decimal.
tupla = ("Alejo Ortiz", "Soy Alejo Ortiz", True, 1.68) #Estos datos no son modificables. 

lista[3] = "Maquinola" #En este caso, la lista es modificable, por lo que se puede cambiar el valor de la posición 3 de la lista.
#tuple[3] = "Maquinola" #En este caso, la tupla no es modificable, por lo que no se puede cambiar el valor de la posición 3 de la tupla.
print (lista[3]) #Imprime el valor de la posición 3 de la lista.

#Creando un conjunto (set) de datos compuestos por diferentes tipos de datos.
conjunto = {"Alejo Ortiz", "Soy Alejo Ortiz", True, 1.68, "Alejo Ortiz"} #Estos datos son como las ''tuplas'', pero no tienen un orden específico ni tampoco se pueden modificar, ni tampoco se puede repetir un valor dentro del conjunto ya que no va a figurar en la consola.
#print (conjunto [1]) No va a funcionar, ya que no se puede acceder a los elementos de un conjunto por su posición.
print (conjunto) #El "Alejo Ortiz" no se va a repetir, ya que no se puede repetir un valor dentro del conjunto.

#Creando un diccionario de datos compuestos por diferentes tipos de datos.
diccionario = { #La estructura del diccionario es clave:valor, donde la clave es un string y el valor puede ser de cualquier tipo de dato.
    "nombre": "Alejo Ortiz",
    "apellido": "Ortiz",
    "edad": 25,
    "altura": 1.68,
    "esta_casado": False,
    "dato_duplicado": "Alejo Ortiz" #El dato duplicado no se va a repetir, ya que no se puede repetir un valor dentro del diccionario.
}
print (diccionario["edad"]) #Imprime el valor de la clave "edad" del diccionario.
print (diccionario["edad"]+2) #Suma 2 al valor de la clave "edad" del diccionario.