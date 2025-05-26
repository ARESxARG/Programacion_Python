A = 1200
B = 800
C = 300
D = 200
E = 1300
F = 1100
Microprocesador = False
Memoria_Ram = False
Teclado = False
Mouse = False
Motherboard = False
Fuente = False
total_productos = 0
contador_RAM = 0
descuentos = 0

print ("Bienvenidos al Sistema de Facturación. A continuación eliga los productos que va a comprar.")
while True:
    productos_seleccionados = input(("\nA) Microprocesador = $1200\nB) Memoria Ram = $800\nC) Teclado = $300\nD) Mouse = $200\nE) Motherboard = $1300\nF) Fuente = $1100\n\nIngrese el producto que desea comprar y para finalizar escriba ''Fin'': "))
    if productos_seleccionados == "A" or productos_seleccionados == "a":
        total_productos = total_productos + A
        Microprocesador = True
    elif productos_seleccionados == "B" or productos_seleccionados == "b":
        total_productos = total_productos + B
        contador_RAM = contador_RAM + 1
        Memoria_Ram = True
    elif productos_seleccionados == "C" or productos_seleccionados == "c":
        total_productos = total_productos + C
        Teclado = True
    elif productos_seleccionados == "D" or productos_seleccionados == "d":
        total_productos = total_productos + D
        Mouse = True
    elif productos_seleccionados == "E" or productos_seleccionados == "e":
        total_productos = total_productos + E
        Motherboard = True
    elif productos_seleccionados == "F" or productos_seleccionados == "f":
        total_productos = total_productos + F
        Fuente = True
    elif productos_seleccionados == "fin" or productos_seleccionados == "Fin":
        break
    else:
        print ("Producto inválido. No seleccionaste ningun producto de la lista.")

if Microprocesador == True and Memoria_Ram == True and Teclado == True and Mouse == True and Motherboard == True and Fuente == True:
    descuentos = descuentos + total_productos * 0.10
    print ("\nLlevaste un kit completo. Descuento del %10 activado.")
if total_productos >= 4000:
    descuentos = descuentos + total_productos *0.10
    print ("Acumulaste $4000 o mas en tu compra. Descuento del %10 activado.")
if contador_RAM >= 3:
    descuentos = descuentos + (contador_RAM // 3) * B
    print ("Promoción 3x2 en Memoria RAM vigente. Descuento activado.")

total_final = total_productos - descuentos

print ("\nEl total a pagar con los descuentos aplicados es de:",total_final)