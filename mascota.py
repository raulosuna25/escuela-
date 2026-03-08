class Mascota:
    
    def __init__(self, nombre, tipo, edad, nivelFelicidad):
        self.nombre = nombre
        self.tipo = tipo
        self.edad = edad
        self.nivelFelicidad = nivelFelicidad

    def alimentar(self):
        self.nivelFelicidad += 10
        if self.nivelFelicidad > 100:
            self.nivelFelicidad = 100

    def jugar(self):
        self.nivelFelicidad += 20
        if self.nivelFelicidad > 100:
            self.nivelFelicidad = 100

    def mostrarEstado(self):
        return f"{self.nombre} es un {self.tipo} con felicidad: {self.nivelFelicidad}"

    def esFeliz(self):
        return self.nivelFelicidad > 70


#  PRUEBAS 

mascota1 = Mascota("Firulais", "Perro", 3, 50)
mascota2 = Mascota("Mishi", "Gato", 2, 75)

print(mascota1.mostrarEstado())
print("¿Es feliz?", mascota1.esFeliz())

mascota1.alimentar()
mascota1.jugar()

print(mascota1.mostrarEstado())
print("¿Es feliz?", mascota1.esFeliz())

print("-------------------")

print(mascota2.mostrarEstado())
mascota2.jugar()
print(mascota2.mostrarEstado())
print("¿Es feliz?", mascota2.esFeliz())