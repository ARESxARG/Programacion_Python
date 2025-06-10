#Ingreso de datos
#El monto sera de tipo float ya que necesitaremos almacenar decimales ejemplo: 79.99$
#La edad es de tipo entero (la edad de una persona no lleva decimales)
#codigo de descuento es una cadena de texto porque los codigos utilizan el mismo tipo de dato ej: "A344B"
print("==== Bienvenido al Sistema de calculo de descuentos ====") #Muestro un mensaje bienvenida
monto_total = float(input("Ingrese el monto total de la compra: "))
edad_comprador = int(input("Ingrese la edad del comprador: "))
codigo_descuento = input("Ingrese el codigo de descuento: ")
descuento_por_edad = 0 # Creo una variable donde voy a guardar el descuento por edad

#Proceso donde voy a calcular el descuento por edad
if edad_comprador < 18: # Si la edad es menor a 18 aplico el descuento
    descuento_por_edad = monto_total * 0.10 # calculo el descuento del 10% del monto total
    print("El descuento por edad es de: ", descuento_por_edad, "$") #Informo el descuento
elif edad_comprador >= 18 and edad_comprador <= 60: #Si la edad esta entre 18 y 60 aplico el descuento
    descuento_por_edad = monto_total * 0.05 # calculo el descuento del 5% del monto total
    print("El descuento por edad es de: ", descuento_por_edad, "$") #Informo el descuento
else: # como no cumple ninguna condicion anterior, entonces la edad es mayor o igual a 60
    descuento_por_edad = monto_total * 0.15 # calculo el descuento del 15% del monto total
    print("El descuento por edad es de: ", descuento_por_edad, "$") #Informo el descuento

#Proceso donde voy a calcular el descuento por codigo de descuento 
#Completar...

#Resultado
print("El monto total con los descuentos es de: ",  monto_total - descuento_por_edad, "$")

#Muestro un mensaje de finalizacion del sistema
print("==== ¡¡Gracias por utilizar nuestro sistema!! :) ====") #Muestro un mensaje bienvenida

