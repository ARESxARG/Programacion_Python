#Ingreso de datos
nombre = input("Ingrese nombre: ")
apellido = input("Ingrese apellido: ")
#Inicializo las constantes donde voy almacenar el nombre
#y apellido del administrador
admin_nombre = "Cristian"
admin_apellido = "Pastrana"

#Proceso
#Si el nombre ingresado es igual al nombre del administrador
#Y si el apellido ingresado es igual al apellido del administrador
#muestro por pantalla que es administrador

#Utlilizando estructuras anidadas (o subestructuras)
if nombre == admin_nombre:
    if apellido == admin_apellido:
        print("es administrador. (Escructura anidada)")
else:
    print("No es administrador. (Escructura anidada)")

#Utilizando operador logico and
if nombre == admin_nombre and apellido == admin_apellido:
        print("es administrador. (Operador logico and)")
else:
    print("No es administrador. (Operador logico and)")






    