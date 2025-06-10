#BUCLE WHILE ¿Como utilizarlo?
#Contar los numeros de 1 a 5
"""valor_inicial = 1
while valor_inicial <= 5: #While lo que hace es imprimir la secuencia debajo, la cantidad de veces que se especifique. En este caso evalua la expresion logica y corta hasta que deje de ser falso (5).
    print(valor_inicial) 
    valor_inicial = valor_inicial + 1 #Para que se actualice al numero siguiente.
print ("Finalizo el bucle ''while''.")"""


#CONSIGNAS 
"""
1) Modificar el programa para que cuente hasta 10.

2) Modificar el programa para que empiece a contar desde 5.

3) Modificar el programa para que muestre de dos en dos.

4) Mostrar solo los multiplos de 2 contando desde 1 a 9.

5) Resolver el ejercicio anterior solicitando: 
Al El usuario ingresara el valor_inicial y el valor_final

6) Un profesor necesita un programa para calcular el promedio de notas de los alumnos:
Solicitar el ingreso de 5 notas.
Indicar si la nota esta aprobada (mayor a 7)
Mostrar cuantas notas estan desaprobadas

7) Escribir un programa donde: 
Se defina una contraseña como constante (ejemplo: "contraseña123").
Se solicite al usuario ingresar su contraseña.
Permitir solo 3 intentos de ingreso de contraseña.
Si la contraseña es correcta, mostrar "acceso valido".
Si la contraseña es incorrecta, solicitarla nuevamente hasta el limite de intentos.
Si supera el limite de intentos, mostrar "acceso invalido".
"""

"""valor_inicial = 5
while valor_inicial <= 10:
    print(valor_inicial) 
    valor_inicial = valor_inicial + 2 #Para que se actualice al numero siguiente.
print ("Finalizo el bucle ''while''.")"""

#Ejercicio 4
"""valor_inicial = 1
while valor_inicial <= 9:
    valor_inicial = valor_inicial + 1
    if valor_inicial % 2 == 0:
        print ("El valor",valor_inicial,"es multiplo de dos.")
print ("Fin del bucle.")"""

#Ejercicio 5
"""valor_inicial = int(input("Ingrese un valor inicial: "))
valor_final = int(input("Ingrese el valor final: "))
while valor_inicial <= valor_final:
    if valor_inicial % 2 == 0:
        print ("El valor",valor_inicial,"es multiplo de dos.")
    valor_inicial = valor_inicial + 1
print ("Fin del bucle.")"""

#Ejercicio 6
"""notas_maxima = 0
desaprobados = 0
notas_ingresadas = 0
notas_alumnos = float(input("Ingrese la nota de 5 alumnos y para finalizar coloque el valor 0: "))
while notas_alumnos != 0:
    notas_maxima += notas_alumnos
    notas_alumnos = float(input("Ingrese el valor de las notas: "))
    print (notas_maxima)
    notas_ingresadas += 1
    if notas_alumnos >= 7:
        print ("El alumno esta aprobado: ",notas_alumnos)
    else:
        desaprobados += 1
else: 
    print (notas_ingresadas)
    print (notas_maxima)
    promedio = notas_maxima / notas_ingresadas
    print ("El promedio de las notas es:",promedio)
    print ("La cantidad de desaprobados es:",desaprobados)"""

#Ejercicio 7
"""contraseña_constante = "contraseña123"
contador_contraseña = 0
while contador_contraseña < 3:
    contraseña_ingresada = input("Ingrese la contraseña válida: ")
    contador_contraseña += 1
    if contraseña_ingresada == contraseña_definida:
        print("Acceso Válido.")
        break #Se utiliza para terminar el programa y cerrar el bucle.
else:
    print (contador_contraseña)
    print ("Acceso Inválido.")"""