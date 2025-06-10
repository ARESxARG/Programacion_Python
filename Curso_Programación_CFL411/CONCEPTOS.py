"""
<<<<<<<<<<<>>>>>>>>>> CONCEPTOS DE PROGRAMACIÓN - CFL411 <<<<<<<<<<<>>>>>>>>>>
"""
#UNIDAD 1
"""
Variables y constantes. Nombres correctos e incorrectos para variables. Como comentar. Como ingresar datos por teclado. Como pedir datos por pantalla al usuario"""

#La función input() en Python se utiliza para pedir al usuario que ingrese datos por teclado. Ejemplo: 
nombre = str(input("Ingresa tu nombre: ")) #Aclaramos el tipo de dato "string"
apellido = str(input("Ingresa tu apellido: ")) #Aclaramos el tipo de dato "string"
print ("Bienvenido al sistema " +nombre,apellido+ " hoy es miercoles") #Otra forma de concatenar la variable es utilizando "," (coma) la misma crea un espacio en la consola
#Ejemplo:
print (nombre+apellido)
print (nombre,apellido)

# Tipos de datos básicos en Python


"""
int     -> Números enteros (sin coma decimal), como 1, -3, 42
float   -> Números reales con coma decimal, como 3.14, -0.5, 2.0
str     -> Cadenas de texto, como "hola", 'Python', "123" (aunque parezca un número, es texto si va entre comillas)
bool    -> Valores lógicos: True o False (¡ojo! con mayúscula)
"""

"""
#Operadores aritméticos
"""
+ = Suma
- = Resta
* = Multiplicación
/ = División
// = Division entera
% = Modulo
** = Potenciación



# ------------------------
# ✅ Tipo de dato booleano
# ------------------------
es_mayor = True
print(es_mayor)  # True
es_mayor = False
print(es_mayor)  # False

# ------------------------------
# ✅ Operadores relacionales
# ------------------------------
# Devuelven valores booleanos: True o False
# Comparaciones básicas:
5 == 5      # True
5 != 5      # False
7 > 4       # True
8 < 2       # False
6 >= 6      # True
4 <= 5      # True

# Ejemplos:
print(5 > 3)       # True
print(2 == 10)     # False
# Uso real con input:
edad = int(input("Ingrese su edad: "))
print("¿Es mayor de edad?:", edad >= 18)

# -----------------------------------------
# ✅ Estructuras condicionales (if / elif / else)
# -----------------------------------------

# Básico con if
if 5 > 3:
    print("Se cumplió la condición")

# Si no se cumple, no se ejecuta nada
if 5 < 3:
    print("Esto no se imprime")

# Importante: respetar la indentación
if 5 < 3:
    print("Esto está dentro del if")

print("Esto está fuera del if")  # Siempre se ejecuta

# Error común: falta de indentación
# if 5 > 3:
# print("Esto rompe el programa")  # ❌ MAL, da error

# Condicional con variable
edad = int(input("Ingrese su edad: "))
if edad >= 18:
    print("Sos mayor de edad")

# ------------------
# ✅ Condicional else
# ------------------

edad = 15
if edad >= 18:
    print("Sos mayor de edad")
else:
    print("No sos mayor de edad")

# ------------------
# ✅ Condicional elif
# ------------------

valor = 5
if valor == 4:
    print("El valor es 4")
elif valor == 5:
    print("El valor es 5")

# Se pueden encadenar varios elif

valor = 6
if valor == 4:
    print("Valor 4")
elif valor == 5:
    print("Valor 5")
elif valor == 6:
    print("Valor 6")

# Con else al final:
valor = 99
if valor == 4:
    print("Valor 4")
elif valor == 5:
    print("Valor 5")
elif valor == 6:
    print("Valor 6")
else:
    print("El valor no es 4, 5 ni 6")


# --------------------
# ✅ Operadores lógicos
# --------------------
# Combinan condiciones

# and → las dos tienen que ser True
edad = 25
tiene_dni = True
if edad >= 18 and tiene_dni:
    print("Puede votar")

# or → al menos una tiene que ser True
es_estudiante = False
es_jubilado = True
if es_estudiante or es_jubilado:
    print("Tiene descuento")

# not → niega el valor
lloviendo = False
if not lloviendo:
    print("Podés salir sin paraguas")
