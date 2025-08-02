class Auto:
    #Atributos
    def __init__(self, color, marca, modelo):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.velocidad = 0
    #Metodos
    def arrancar(self):
        return "El auto: " + self.marca + " modelo: " + self.modelo + " ha arrancado."
    def frenar(self):
        return "El auto: " + self.marca + " modelo: " + self.modelo + " ha frenado."
    def acelerar(self):
        self.velocidad += 10
        return "La velocidad actual es: " + str(self.velocidad) + " km/h"

mi_auto = Auto("rojo", "Ford", "Fiesta")
tu_auto = Auto("azul", "Toyota", "Corolla")

print(mi_auto.color)    # Salida: rojo
print(tu_auto.marca)    # Salida: Toyota

print(mi_auto.arrancar()) # Salida: El Ford Fiesta de color rojo ha arrancado.
print(tu_auto.frenar())   # Salida: El Toyota Corolla de color azul ha frenado.




class Conductor:
    def __init__(self, nombre):
        self.nombre = nombre
    def encender_auto(self, auto):
        print(f"{self.nombre} está intentando encender el auto.")
        print(auto.arrancar()) # El Conductor envía un mensaje (llama al método arrancar) al objeto Auto
    def aumentar_velocidad(self,auto):
        print(f"{self.nombre} apreta el acelerador")
        print(auto.acelerar())

mi_conductor = Conductor("Juan")
mi_conductor.encender_auto(mi_auto)
mi_conductor.aumentar_velocidad(mi_auto)
mi_conductor.aumentar_velocidad(mi_auto)
mi_conductor.aumentar_velocidad(mi_auto)

# Salida:
# Juan está intentando encender el auto.
# El Ford Fiesta de color rojo ha arrancado.