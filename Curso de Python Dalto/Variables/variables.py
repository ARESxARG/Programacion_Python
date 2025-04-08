#Variables. Las variables son valores que definimos, se guardan en memoria y se utilizan para almacenar datos.

#Definendo una variable con camelCase.
nombreCompleto = "Pedrito"

#Definendo una variable con snake_case. Recomendación oficial de PEP 8 (Guía de estilo para Python).
nombre_completo = "Pedrito"

nombre = "Alejo" #''Nombre'' es una variable de tipo string
edad = 25 #''Edad'' es una variable de tipo int
estatura = 1.68 #''Estatura'' es una variable de tipo float
es_mayor_de_edad = True #''Es mayor de edad'' es una variable de tipo bool
print (nombre) #Imprime el valor de la variable ''nombre''
print (edad) #Imprime el valor de la variable ''edad''  
print (estatura) #Imprime el valor de la variable ''estatura''
print (es_mayor_de_edad) #Imprime el valor de la variable ''es mayor de edad''

#Concatenar Variables. En Python, para concatenar variables de tipo string e int, se debe convertir el int a string utilizando la función str(). Para hacerlo se utliza el operador + el nombre de la variable a concatenar. 
nombre = "Alejo"
edad = 25
print ("Hola, mi nombre es " + nombre + " y tengo " + str(edad) + " años.") #Concatenar variables de tipo string e int

#Otra forma de concatenar variables es utilizando la f-string, que permite insertar variables dentro de una cadena de texto utilizando llaves {}. Para hacerlo se utiliza la letra f antes de la cadena de texto.
nombre = "Alejo"
edad = 25
bienvenida = f"Hola, mi nombre es {nombre} y tengo {edad} años." #Concatenar variables de tipo string e int utilizando f-string.
print (bienvenida) #Imprime el valor de la variable ''bienvenida''

#Se utilizan los operadores de pertenencia "not in" o "in" para verificar si un elemento se encuentra dentro de una lista o no.
ejemplo_lista = [1, 2, 3, 4, 5]
print(1 in ejemplo_lista) #En la consola, una vez ejecutemos nuestro código nos figurará ''True''
print(6 in ejemplo_lista) #En la consola, una vez ejecutemos nuestro código nos figurará ''False''
print(1 not in ejemplo_lista) #En la consola, una vez ejecutemos nuestro código nos figurará ''False''
print(6 not in ejemplo_lista) #En la consola, una vez ejecutemos nuestro código nos figurará ''True''