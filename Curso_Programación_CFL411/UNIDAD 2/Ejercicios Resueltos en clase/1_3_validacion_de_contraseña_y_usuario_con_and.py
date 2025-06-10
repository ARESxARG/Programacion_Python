#Al ejercicio 2.6 de la guia 2 se pide tambien validar el usuario "pedro"
#Inicializo las variales usuario y contraseña
mensaje_bienvenida = "Bienvenido al sistema: "
usuario = "pedro"
contraseña = "secreta123"
#Solicito el ingreso de datos del usuario y contraseña
usuario_ingresado = input("Ingrese usuario: ")
contraseña_ingresada = input("Ingrese contraseña: ")
#Evaluo si la contraseña ingresada es igual a contraseña
#Y si el usuario ingresado es igual a usuario
if contraseña_ingresada == contraseña and usuario_ingresado == usuario:
    print("Accesso Valido" , mensaje_bienvenida, usuario)
else:
    print("Acceso invalido")


