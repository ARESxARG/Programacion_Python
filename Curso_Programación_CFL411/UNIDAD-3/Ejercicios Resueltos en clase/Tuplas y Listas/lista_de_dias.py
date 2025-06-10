#Modifico el dia miercoles por "Pedro" y agrego un dia mas con el nombre "Cristian"
lista_dias = ["Lunes", "martes" ,"miercoles","jueves","viernes"]
lista_dias[2] = "Pedro"
dia_cristian = ["Cristian"]
lista_dias = lista_dias + dia_cristian #  ["Lunes", "martes" ,"miercoles","jueves","viernes"] + ["Cristian"] 
for elemento in lista_dias:
    print("El dia es :", elemento)

