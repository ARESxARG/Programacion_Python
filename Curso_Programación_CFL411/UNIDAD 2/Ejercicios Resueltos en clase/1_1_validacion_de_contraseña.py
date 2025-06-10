#Ingreso de datos
contraseña_usuario = input("Ingrese su contraseña: ")
contraseña_almacenada = "secreta123"
#Proceso
#Si la contraseña ingresada es igual a la contraseña almacenda
#Muestro por pantalla que la contraseña es correcta
#Caso contrario se muestra el mensaje contraseña incorrecta
if contraseña_usuario == contraseña_almacenada:
    print("Contrasenia correcta")
if contraseña_usuario != contraseña_almacenada:
    print("Contrasenia incorrecta")

