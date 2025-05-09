#Unidad 3. Temas :
"""
Bucle while
Contadores y acumuladores
Bucle for
"""
#Ejemplo de un Acumulador:
valor_inicial = 1
while valor_inicial <= 5:
    print (valor_inicial)
    valor_inicial += 1

#Ejemplo de Contador y Acumulador
contador = 1
acumulador = 0
while contador <= 5:
    print ("Contador:",contador)
    acumulador += contador 
    contador += 1
else:
    print ("La suma de los valores es: ",acumulador)

#Otra forma mas comoda para poder parar el bucle utilizando un un contador en vez de un valor (en vez de 0).
#Hecho en clase por el profe
contador_notas = 1 #Aclaramos el valor "1" para poder llegar al valor estimado.
contador_desaprobados = 0 #Aclaramos la variable para acumularla
acumulador_notas = 0
while contador_notas <= 5:
    nota_estudiante = int(input("Ingrese la nota: "))
    acumulador_notas += nota_estudiante #Con esto sumamos las cantidades que se ingresen de las notas
    if nota_estudiante >= 7:
        print ("El alumno esta aprobado.")
    else:
        print ("El alumno esta desaprobado.")
        contador_desaprobados +=1
    contador_notas +=1 #Esto cuenta la cantidad de notas desaprobadas
else:
    print ("La cantidad de desaprobados es:",contador_desaprobados)
    print ("El estudiante tiene un promedio de: ",acumulador_notas / 5)

#Ejercicio 7 Hecho en clase por el profe
CONTRASEÑA = "contraseña123" #Se escribe en mayuscula ya que es una variable CONSTANTE.
contador = 1
while contador <= 3:
    contraseña_nueva = input("Ingrese la contraseña válida: ")
    if contraseña_nueva == CONTRASEÑA:
        print("Acceso Válido.")
        break #Se utiliza para terminar el programa y cerrar el bucle.
    else:
        print ("Acceso Inválido.")
    contador += 1