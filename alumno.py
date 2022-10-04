class Alumno():
    nombre = None
    calificacion = None

    def __init__(self, nombre, calificacion):
        self.nombre = nombre
        self.calificacion = calificacion

    def mostrarAlumno(self):
        print("Nombre: ", self.nombre)
        print("Calificacion: ", self.calificacion)

    def aprobacion(self):
        if self.calificacion > 7:
            print("Aprobado.")
        else: 
            print("No aprobado.")

alumno1 = Alumno("Xavier", 8)
alumno1.mostrarAlumno()
alumno1.aprobacion()
