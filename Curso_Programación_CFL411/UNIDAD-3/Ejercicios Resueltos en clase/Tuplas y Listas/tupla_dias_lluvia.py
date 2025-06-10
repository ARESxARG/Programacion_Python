tupla_dias_lluvia = (False,True,True,False,False) #Tupla de 4 elementos
for elemento in tupla_dias_lluvia:
    if elemento == False:#  False == False ,  True == False, True == False, ....
        print("no llovio")
    else:
        print("si llovio")
