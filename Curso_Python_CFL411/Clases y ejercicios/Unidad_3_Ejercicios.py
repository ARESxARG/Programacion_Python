#Ejercicio 3.1 Escribir un programa que muestre los numeros del 1 al 10.
"""contador = 1
while contador <= 5:
    print ("El contador vale:",contador)
    contador +=1
else:
    print ("Fin del programa.")"""

#Ejercicio 3.2. Escribir un programa que sume los numeros del 1 al 5 y muestre el total.
"""contador = 1
acumulador = 0
while contador <= 5:
    print ("El contador vale:",contador)
    acumulador += contador #Cambiar de lugar el acumulador para poder realizar la iteración correctamente.
    contador +=1
else:
    print ("Fin del programa. El contador total vale :",acumulador)"""

#3.3. Escribir un programa que pida el ingreso de un numero y muestre la tabla de multiplicar de 1 hasta 10 de ese numero.
"""contador_para_tabla = 1
numero = int(input("Ingresar un numero para mostrar su tabla de multiplicación: "))
while contador_para_tabla <= 10:
    print (numero,"*",contador_para_tabla,"es igual a:",numero*contador_para_tabla) #Mostrar el numero directamente en el contador para tabla en vez de hacer una variable aparte.
    contador_para_tabla +=1
print ("\nFin del programa.")"""

#3.4. Escribir un programa donde el usuario debe adivinar un numero secreto entre 1 y 10
"""NUMERO_SECRETO = 7
numero = int(input("¿Cual es mi numero secreto? Ingrese un numero del 1 al 10 para adivinarlo: "))
while numero != NUMERO_SECRETO:
    numero = int(input("Numero secreto incorrecto. Ingrese un valor nuevamente: "))
else:
    print (">>>>> Adivinaste el numero secreto. Recompensa final : FIN DEL BUCLE. <<<<<")"""

#3.5. Escribir un programa que muestre los números desde 1 hasta 10.
"""for numeros in range(1,11): #range() crea una secuencia iterable de 1 hasta 5 
    print(numeros)"""

#3.6. Escribir un programa que sume los números pares que hay desde 1 hasta 10. 
"""acumulador = 0
for iterador in range (1,11): #Imprime en la terminal los valores del rango establecido
    if (iterador % 2) == 0:
        acumulador += iterador
else:
    print ("La suma total es:",acumulador)"""

#3.7. Escribir un programa que pida el ingreso de un numero y muestre por pantalla los números desde 1 hasta el ingresado por el usuario.
"""numero_ingresado = int(input("Ingrese un numero mayor a 1: "))
for iterador in range (1,numero_ingresado):
    print (iterador)"""

#3.8 Escribir un programa que pida el ingreso de un número y muestra la suma de todos los números que hay  entre 1 y el numero ingresado.
"""acumulador = 0
numero_ingresado = int(input("Ingrese un numero aleatorio: "))
for iterador in range (1,numero_ingresado):
    acumulador += iterador + numero_ingresado
print ("La suma total es:",acumulador)"""

#3.9 Crear una tupla que almacene los días de la semana y mostrar por pantalla el día  miércoles utilizando el índice que apunta a ese elemento.
"""tupla_dias_de_semana = ("lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo")
print ("Dia de la semana:",(tupla_dias_de_semana[2]))"""

#3.10 Crear una tupla que almacene el nombre de un estudiante y una nota. Indicar si el estudiante está aprobado (nota mayor o igual a 7) 
"""tupla_alumno = ("David", 7)
if tupla_alumno[1] >= 7:
    print ("El alumno se encuentra aprobado.")
else:
    print ("El alumno esta desaprobado.")"""

#3.11  Crear  una  tupla  que  almacene  las  asignaturas  de  un  curso  (por ejemplo, matemáticas, Física, Química e Historia) y muestre por pantalla cada una de ellas por separado. 
"""tupla_materias = ("Matemática","Biología","Psicología","Introducción a Pensamiento Científico")
for iterador in tupla_materias:
    print (iterador)"""

#3.12  Crear  una  lista  que  almacene  nombres  de  estudiantes  y  mostrar  el  ultimo estudiante utilizando el índice que apunta a ese elemento. 
"""lista_alumnos = ["Ludmila","Ariel","Marina","Tobias","Alejo"]
print (lista_alumnos[4])"""

#3.13  Crear  una  lista que almacene  nombres de estudiantes,  cambiar el  nombre  del último estudiante por “Pedro” y mostrarlo por pantalla.
"""lista_alumnos = ["Ludmila","Ariel","Marina","Tobias","Alejo"]
lista_alumnos[4] = "Roberto"
print (lista_alumnos[4])"""

#3.14 Crear una lista que almacene 5 números enteros y mostrar por pantalla solo los números pares
"""lista_numeros = [22, 35, 21, 50, 31]
for iterador in lista_numeros:
    if (iterador % 2) == 0:
        print ("El numero",iterador,"es par.")"""

#3.15 Crear una lista que almacene 5 números enteros y mostrar por pantalla solo el mayor 
lista_numeros = [9, 12, 3, 1, 21]
print (lista_numeros[4])

#3.16 Escribir un programa que modifique recorra una lista y si el numero es negativo debe modificarlo por el mismo valor, pero positivo.
"""lista_numeros = [-2,4,5,-13,11]
print ("Lista de numeros antes de la modificación:",lista_numeros)
for iterador in lista_numeros:
    if iterador < 0:
        lista_numeros[0] = 2
        lista_numeros[3] = 13
print ("Lista de numeros despues de la modificación:",lista_numeros)"""