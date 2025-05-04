#Ejercicio Obligatorio IF-ELIF-ELSE
año = int(input("Ingrese un año para determinar si es bisiesto o no: "))
if (año % 4) != 0:
    print ("El año",año,"no es bisiesto, ya que no es divisible por 4.")
elif (año % 100) == 0 and (año % 400) != 0:
    print ("El año",año,"es divisible entre 100, pero no entre 400, por lo tanto no es un año bisiesto.")
else:
    print (año,"es un año bisiesto.")
