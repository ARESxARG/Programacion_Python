#Carga de los estudiantes
tupla_estudiantes = []
while True:
    nombre = input("Ingrese el nombre del estudiante: ")
    nota = int(input("Ingrese la nota del estudiante (1-10): "))
    while nota < 1 or nota > 10:
        nota = int(input("La nota no es valida, reingrese la nota del estudiante (1-10): "))
    estudiante = (nombre, nota)
    tupla_estudiantes.append(estudiante)
    respuesta_usuario = input("Desea continuar con la carga (si/no): ")
    if respuesta_usuario != "si":
        break
print(tupla_estudiantes)
#Menu de opciones
while True:
    print("======Menu======")
    print("1. Ver todos los estudiantes y sus notas.")
    print("2. Ver el promedio general de notas.")
    print("3. Ver estudiantes aprobados.")
    print("4. Ver estudiantes desaprobados.")
    print("5. Finalizar el programa.")
    opcion = int(input("Ingrese una de las opciones validas (1-5): "))
    if opcion == 1:
        for estudiante in tupla_estudiantes:
            print("nombre del estudiante: ", estudiante[0])
            print("nota del estudiante: ", estudiante[1])
    elif opcion == 2:
        cantidad_estudiantes = len(tupla_estudiantes)
        acumulador_notas = 0
        for estudiante in tupla_estudiantes:
            acumulador_notas += estudiante[1]
        promedio = acumulador_notas / cantidad_estudiantes
        print("El promedio de la nota de los alumnos es: ", promedio)
    elif opcion == 3:
        for estudiante in tupla_estudiantes:
            if estudiante[1] >= 7:
                print("El estudiante:",estudiante[0],"esta aprobado.")
    elif opcion == 4:
        for estudiante in tupla_estudiantes:
            if estudiante[1] <= 6 :
                print("El estudiante:",estudiante[0],"esta desaprobado.")
    elif opcion == 5:
        break
    else:
        print("La opcion ingresada no es valida, debe estar comprendida entre 1 y 5")