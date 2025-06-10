#Contar los numeros de 1 a 5
#1) modificar el programa para que cuente hasta 10
#2) modificar el programa para que comience a contar desde 5
#3) modificar el programa para que muestre de dos en dos
#4) mostrar solo los multiplos de 2 contando desde 1 a 9
#5) resolver el ejercicio anterior solicitando
#   al usuario ingresar valor_inicial y valor_final
#6)Un profesor necesita un programa para calcular el promedio
#  de notas para un alumno.
#  *Solicitar el ingreso de 5 notas
#  *Indicar si la nota esta aprobada (si es mayor a 7)
#  *Mostrar cuantas notas estan desaprobadas
#  *Mostrar el promedio de las notas
#7) Escribir un programa donde:
# *Se defina una contraseña como constante (ejemplo: "contraseña123")
# *Se solicite al usuario ingresar su contraseña
# *Permitir solo 3 intentos de ingreso de contraseña
# *Si la contraseña es correcta, mostrar "acceso valido"
# *Si la contraseña es incorrecta, solicitarla nuevamente hasta el limite de intentos
# *Si supera el limite de intentos, mostrar "acceso invalido"
contador = 1
acumulador = 0 
while contador <= 5 :
    print(contador)
    acumulador += contador
    contador += 1 
else:
    print("La suma de todos los valores es:", acumulador)
print("finalizo el bucle")
