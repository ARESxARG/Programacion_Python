#Calculadora o conversor de tiempo a salario neto
print ("Bienvenidos al sistema de conversión laboral.")
#Datos a pedir
horas_trabajadas = int(input("\nIngrese cantidad de horas trabajadas al día: "))
dias_trabajados = int(input("Ingrese la cantidad de días semanales trabajados: "))
salario_neto = float(input("Ingrese en números su salario neto: "))
salario_por_hora = float(input("Ingrese el monto del salario por hora: "))
#Cálculos/Conversión
conversion_semanal = horas_trabajadas*dias_trabajados #Horas trabajadas semanalmente
conversion_mensual = float(conversion_semanal*4.33) #Horas trabajadas mensualmente
conversion_por_hora = (salario_neto/conversion_mensual) #Salario por hora
conversion_hora_a_mensual = (salario_por_hora*conversion_mensual) #Salario mensual segun las horas
conversion_hora_a_semanal = (salario_por_hora*conversion_semanal) #Salario semanal segun las horas
#Dato final
print (f"El tiempo trabajado semanalmente es de {conversion_semanal} horas")
print (f"El tiempo trabajado mensualmente es de {conversion_mensual} horas")
print (f"El salario es ${conversion_por_hora} por hora")
print (f"El salario mensual es de ${conversion_hora_a_mensual} pesos")
print (f"El salario semanal es de ${conversion_hora_a_semanal} pesos")