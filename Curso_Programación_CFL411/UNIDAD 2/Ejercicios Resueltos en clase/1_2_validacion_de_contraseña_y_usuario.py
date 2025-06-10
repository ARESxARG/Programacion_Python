#Inicializo las variales usuario y contraseña
usuario = "pedro"
contraseña = "secreta123"
#Solicito el ingreso de datos del usuario y contraseña
usuario_ingresado = input("Ingrese usuario: ")
contraseña_ingresada = input("Ingrese contraseña: ")
#Evaluo si la contraseña ingresada es igual a contraseña
if contraseña_ingresada == contraseña:
    print("Contraseña valida")
else:
    print("Contraseña incorrecta")
#Evaluo si el usuario ingresado es igual usuario
if usuario_ingresado == usuario:
    print("Nombre de usuario correcto")
else:
    print("Nomre de usuario incorrecto")

