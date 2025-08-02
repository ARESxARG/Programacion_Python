"""
<<<<<<<<<< UNIDAD 5 PROGRAMACIÓN ORIENTADA A OBJETOS >>>>>>>>>>
"""
#Ejercicio 5.1
"""class Empleado: 
    #Atributos 
    def __init__(self, nombre, apellido, sueldo): 
        self.nombre = nombre 
        self.apellido = apellido 
        self.sueldo = sueldo
    #Método
    def mostrar_informacion(self):
        return f"El empleado se llama {self.nombre}, se apellida {self.apellido} y su sueldo es de ${self.sueldo}"""

#Ejercicio 5.2
class Persona:  
    def __init__(self, nombre, edad): 
        self.nombre = nombre 
        self.edad = edad
    def mostrar_edad(self):
        return f"La persona se llama {self.nombre} y tiene {self.edad} años de edad."
    def cumplir_años(self):
        self.edad += 1
        return f"{self.nombre} cumplió {self.edad} años de edad."

persona1 = Persona("Alejo", 25)
print (persona1.cumplir_años())