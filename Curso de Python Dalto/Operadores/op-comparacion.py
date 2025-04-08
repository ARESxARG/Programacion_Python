#Comparadores. Sirven para comparar valores y devolver un booleano.

#¿De que manera escribo los comparadores?
# "<=" o ">=" : Se escribe primero con "<" o "Shift+ >" y seguido del "=".
# "!=" : Se escribe con "!" y seguido del "=".
# "==" : Se escribe con "=" y seguido del "=". 
es_igual_que = 5 == 6 #False
es_diferente_que = 5 != 6 #True

#Mayor ">" hacia la izquierda.
es_mayor_que = 5 > 6 #False
es_mayor_igual_que = 5 >= 6 #False

#Menor "<" hacia la derecha.
es_menor_que = 5 < 6 #True
es_menor_igual_que = 5 <= 6 #True
print (es_diferente_que) #Mostraria en resultado False en la consola.

#Ejemplo de comparacion de variables con calculos combinados.
a = 5
b = 10
c = 20
comparacion = a + b == c
print(comparacion) #Mostraria en resultado False en la consola.

#Ejemplo de comparación para verificar usuarios.
usuario_de_base_de_datos = "Alejo Ortiz"
usuario_ingresado = "Alejo"
print(usuario_de_base_de_datos == usuario_ingresado)

#Ejemplo2
contraseña_almacenada = "1234"
contraseña_ingresada = "12345"
print(contraseña_almacenada == contraseña_ingresada)