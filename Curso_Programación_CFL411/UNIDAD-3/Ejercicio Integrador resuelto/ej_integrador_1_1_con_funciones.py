#Carga de los estudiantes
lista_estudiantes = []
while True:
    nombre = input("Ingrese el nombre del estudiante: ")
    nota = int(input("Ingrese la nota del estudiante (1-10): "))
    while nota < 1 or nota > 10:
        nota = int(input("La nota no es valida, reingrese la nota del estudiante (1-10): "))
    estudiante = (nombre, nota)
    lista_estudiantes.append(estudiante)
    respuesta_usuario = input("Desea continuar con la carga (si/no): ")
    if respuesta_usuario != "si":
        break
print(lista_estudiantes)
#Funcion para mostrar el menu
def mostrar_menu():
    print("===========Menu===============")
    print("1. Ver todos los estudiantes y sus notas.")
    print("2. Ver el promedio general de notas.")
    print("3. Ver estudiantes aprobados.")
    print("4. Ver estudiantes desaprobados.")
    print("5. Finalizar el programa.")
    print("=============================")

#Funcion para mostrar estudiantes
def mostrar_estudiantes(lista_estudiantes):
    for estudiante in lista_estudiantes:
        print("nombre del estudiante: ", estudiante[0])
        print("nota del estudiante: ", estudiante[1])

#Funcion para calcular el promedio
def mostrar_promedio(lista_estudiantes):
    cantidad_estudiantes = len(lista_estudiantes)
    acumulador_notas = 0
    for estudiante in lista_estudiantes:
        acumulador_notas += estudiante[1]
    promedio = acumulador_notas / cantidad_estudiantes
    print("El promedio de la nota de los alumnos es: ", promedio)

#Funcion para mostrar aprobados
def mostrar_aprobados(lista_estudiantes):
    for estudiante in lista_estudiantes:
        if estudiante[1] >= 7:
            print("El estudiante:",estudiante[0],"esta aprobado.")

#Funcion para mostrar desaprobados
def mostrar_desaprobados(lista_estudiantes):
    for estudiante in lista_estudiantes:
        if estudiante[1] <= 6 :
            print("El estudiante:",estudiante[0],"esta desaprobado.")


#Menu de opciones
while True:
    mostrar_menu()
    opcion = int(input("Ingrese una de las opciones validas (1-5): "))
    if opcion == 1:
        mostrar_estudiantes(lista_estudiantes)
    elif opcion == 2:
        mostrar_promedio(lista_estudiantes)
    elif opcion == 3:
        mostrar_aprobados(lista_estudiantes)
    elif opcion == 4:
        mostrar_desaprobados(lista_estudiantes)
    elif opcion == 5:
        break
    else:
        print("La opcion ingresada no es valida, debe estar comprendida entre 1 y 5")