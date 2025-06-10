#4.1  Crear  un  diccionario  que  almacene  el  stock  de  3  productos  de  una  frutería  y mostrarlo por pantalla. 
"""productos = {"Manzanas" : 5,
             "Duraznos" : 5,
             "Peras" : 5
}
print (productos)"""

#4.2 Mostrar por pantalla el stock de alguno de los productos.   
"""productos = {"Manzanas" : 5,
             "Duraznos" : 5,
             "Peras" : 5
}
print ("El stock de los duraznos es de:",productos["Duraznos"])"""

#4.3 Agregar  un  nuevo  producto  al  diccionario  y  mostrar  por  pantalla  el  diccionario actualizado. 
"""productos = {"Manzanas" : 5,
             "Duraznos" : 5,
             "Peras" : 5
}
productos["Bananas"] = 5
print (productos)"""

#4.4 Modificar el stock de alguno de los productos y mostrar por pantalla el diccionario actualizado. 
"""productos = {"Manzanas" : 5,
             "Duraznos" : 5,
             "Peras" : 5
}
productos["Peras"] = 0
print (productos)"""

#4.5 Eliminar alguno de los productos y mostrar por pantalla el diccionario actualizado. 
"""productos = {"Manzanas" : 5,
             "Duraznos" : 5,
             "Peras" : 5
}
productos.pop("Manzanas")
print (productos)"""

#4.6 Escribir un programa que solicite el nombre y la edad a una persona (validar que la edad  no  sea  negativa). Luego  debe  guardar  esa  información  en  un  diccionario  y mostrarlo por pantalla. 
"""datos = {}
nombre = input("Ingrese el nombre de la persona: ")
edad = int(input("Ingrese la edad de la persona: "))
while edad < 0:
    edad = int(input("Error de sintaxis. Ingrese la edad nuevamente: "))
datos[nombre] = edad
print (datos)"""

#4.7 Escribir un programa que cargue las notas de los alumnos en un diccionario. Se deben cumplir los siguientes requisitos: 
# • Solicitar al usuario que ingrese el nombre de un alumno. 
# • Solicitar al usuario que ingrese la nota del alumno. 
# • Guardar  la  información  ingresada  en  un  diccionario  donde  la  clave  será  el nombre del alumno y el valor será la nota. 
# • La carga debe continuar hasta que el usuario ingrese “salir” como nombre. 
# • Al  finalizar  la  carga,  mostrar  por  pantalla  el  diccionario  con  todas  las  notas cargadas.
"""datos = {}
while True:
    alumno = input("Ingrese el nombre del alumno: ")
    if alumno == "salir" or alumno == "Salir" or alumno == "SALIR":
        break
    nota = int(input("Ingrese la nota del alumno: "))
    datos[alumno] = nota
print (datos)"""

"""
<<<<<<<<<<>>>>>>>>>> FUNCIONES <<<<<<<<<<>>>>>>>>>>
"""
#4.8  Definir  una  funciona  llamada  saludar  que  reciba  un  nombre  como  parámetro  y muestre por pantalla un saludo. Ejemplo “Hola, Cristian”. 
"""def saludar(nombre):
    print("Hola,", nombre)
saludar("River")"""

#4.9  Definir  una función  llamada sumar  que reciba  dos  números  como parámetros  y retorne la suma de ambos. 
"""def sumar(a, b):
    return a + b
resultado = sumar(10, 5)
print("La suma es:",resultado)"""

#4.10 Definir una función llamada retornar_mayor que reciba que reciba dos números como parámetros y retorne el número mayor. 
"""def retornar_mayor(a, b):
    if a > b:
        return a
    else:
        return b
mayor = retornar_mayor(21, 9)
print("El mayor es:", mayor)"""

#4.11 Definir una función que reciba dos cadenas de texto como parámetros y retorne la cadena con más caracteres. 

#4.12 Definir una función que reciba una palabra y una letra como parametros y retorne cuantas veces se repite la letra dentro de la palabra.

#4.13 Definir una función que reciba una lista de números como parámetro y retorne el mayor de los números de la lista. 

#4.14 Definir una función que reciba una lista de números como parámetro y retorne una nueva lista sin números repetidos. 

#4.15 Se necesita almacenar la información asociada a 3 estudiantes en una lista de diccionarios. Escribir un programa que: 
# • Solicite el ingreso de nombre, apellido y edad de un estudiante. 
# • Almacene esa información en un diccionario. 
# • Luego  de  cargar  un  estudiante  el  diccionario  debe  agregarse  a  una  lista  de estudiantes. 
# • Cuando finalice la carga de los 3 estudiantes debe mostrarse por pantalla la lista de estudiantes con la información cargada.