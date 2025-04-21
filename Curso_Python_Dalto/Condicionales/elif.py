#Ejemplo de uso de elif
ingreso_mensual = 81000 #Definimos una variable con el ingreso mensual de una persona X
gasto_mensual = 80000 #Definimos una variable con el gasto mensual de la misma persona X

#Ejemplo práctico de uso de if, elif y else anidados
if ingreso_mensual > 10000: #Primer condicion
    if ingreso_mensual - gasto_mensual < 0:
        print ("Estas en déficit")
    elif ingreso_mensual - gasto_mensual > 3000:
        print ("Andas bien, tenes superavit")
    else:
        print ("Estas gastando mas de lo que ganas, hay que ver si te alcanza para vivir")


elif ingreso_mensual > 1000: #Utilizamos elif para agregar mas de una condicion
    print ("Vivis re bien en Argentina")
elif ingreso_mensual > 500 :
    print ("Estas re bien economicamente, pero no tanto como para vivir en Suiza")
elif ingreso_mensual > 200 :
    print ("Podes vivir con lo básico en Africa") 
#Se puede agregar tantas condiciones como se desee utilizando elif.

else : #Si no se cumple ninguna de las condiciones anteriores se ejecuta el else
    print ("Sos re pobre")
