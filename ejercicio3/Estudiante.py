class Estudiante:
    def __init__(self, nombre, edad, carrera):
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera
        self.calificaciones = []

    # Agregar una calificación con validación
    def agregarCalificacion(self, calificacion):
        if 0 <= calificacion <= 100:
            self.calificaciones.append(calificacion)
        else:
            print(f"❌ Calificación inválida: {calificacion}")

    # Agregar varias calificaciones
    def agregarVariasCalificaciones(self, lista):
        for cal in lista:
            self.agregarCalificacion(cal)

    # Calcular promedio
    def calcularPromedio(self):
        if not self.calificaciones:
            return 0
        return sum(self.calificaciones) / len(self.calificaciones)

    # Mostrar toda la información
    def mostrarInformacion(self):
        promedio = self.calcularPromedio()
        return (
            f"Nombre: {self.nombre}\n"
            f"Edad: {self.edad}\n"
            f"Carrera: {self.carrera}\n"
            f"Calificaciones: {self.calificaciones}\n"
            f"Promedio: {promedio:.2f}\n"
        )

    # Método especial (nivel pro)
    def __str__(self):
        return f"{self.nombre} - {self.carrera} (Promedio: {self.calcularPromedio():.2f})"


# Crear estudiantes
estudiante1 = Estudiante("Raul", 30, "Ing. en sistemas")
estudiante2 = Estudiante("Fatima", 25, "Ing. en Industrial")
estudiante3 = Estudiante("Dayana", 20, "Ing. en Electrónica")

# Agregar calificaciones
estudiante1.agregarVariasCalificaciones([100, 50, 40])
estudiante2.agregarVariasCalificaciones([90, 80, 110])  # 110 es inválida

# Mostrar información completa
print("📊 INFORMACIÓN COMPLETA\n")
print(estudiante1.mostrarInformacion())
print(estudiante2.mostrarInformacion())
print(estudiante3.mostrarInformacion())

# Uso del método especial __str__
print("📌 RESUMEN")
print(estudiante1)
print(estudiante2)
print(estudiante3)
