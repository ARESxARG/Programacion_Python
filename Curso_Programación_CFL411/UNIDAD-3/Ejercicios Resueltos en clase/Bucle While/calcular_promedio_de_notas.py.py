#6)Un profesor necesita un programa para calcular el promedio
#  de notas para un alumno.
#  *Solicitar el ingreso de 5 notas
#  *Indicar si la nota esta aprobada (si es mayor a 7)
#  *Mostrar cuantas notas estan desaprobadas
#  *Mostrar el promedio de las notas
contador_notas = 1
contador_desaprobados = 0
acumulador_notas = 0 
while contador_notas <= 5: #Mientras contador_notas sea menor o igual a 5
    nota_estudiante = int(input("Ingrese la nota: ")) #Pido el ingreso de la nota
    acumulador_notas += nota_estudiante # acumulo las notas para luego calcular el promedio cuando finalice el bucle
    if nota_estudiante >= 7: #Si la nota del estudiante es mayor o igual a 7
        print("Esta aprobado.") #Muestro que esta aprobado
    else: #Caso contrario entonces esta desaprobado
        print("Esta desaprobado") #Muestro que esta desaprobado
        contador_desaprobados += 1 #Incremento el contador de desaprobados para poder mostrarlo cuando finalice el bucle
    contador_notas += 1 #Incremento el contador de notas
else: # Cuando finaliza el bucle while se ejecuta el bloque else con los datos almacenados
    #print(acumulador_notas)
    #print(contador_notas - 1)
    print("La cantidad de desaprobados es:", contador_desaprobados)
    print("El estudiante tiene un promedio de:",acumulador_notas / (contador_notas - 1) ) 
    #Tener en cuenta que contador_notas cuando finalice el bucle tendra un valor de 6
    #Entonces lo conveniente sera restar 1 a contador_notas