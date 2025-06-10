#Por medio de la tabla ascii Python puede determinar
#si una letra es mayor o menor a otra
#En la tabla ascii la letra "a" tiene el valor 97
#y la letra "z" tiene el valor 122
letra = "m" # La letra "m" tiene el valor 109
print(letra >= "a" and letra <= "z") 
#Cuando python interpreta la linea de codigo anterior,
#lo que hace es reemplazar los caracteres por sus valores en la tabla ascii
#print(109 >= 97 and 109 <= 122)
#lo anterior da como resultado True entonces la letra "m" se encuentra en el abecedario
#Link a la web con la tabla: https://elcodigoascii.com.ar/