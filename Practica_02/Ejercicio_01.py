import datetime


# Función para mostrar la fecha y hora
def mostrar_fecha_registro(fecha):
    # Mostramos la fecha con precisión de minutos
    print("Fecha y hora de registro: {}".format(fecha.strftime("%Y-%m-%d %H:%M")))


class Persona:
# 1. Atributo de clase compartido
    nacionalidad = "Peruana"

# Constructor
    def __init__(self, saldo=0.0):
        self.nombre = ""
        self.edad = 0
        self.saldo = saldo
        self.fecha_registro = datetime.datetime.now()

# Metodo para registrar datos mediante consola
    def registrar(self):
        self.nombre = input("Ingrese el nombre de la persona: ")

        while True:
            try:
                edad_ingresada = int(input("Ingrese la edad de {}: ".format(self.nombre)))

                if edad_ingresada >= 0:
                    self.edad = edad_ingresada
                    print("Registro exitoso.")
                    break
                else:
                    print("Error: La edad no puede ser negativa.")
            except ValueError:
                print("Error: debe ingresar un número entero válido.")

# Metodo para incrementar la edad
    def cumpleaños(self):
        self.edad += 1
        print("¡Feliz cumpleaños {}! Ahora tienes {} años.".format(self.nombre, self.edad))


# Pruebas Ejercicio 1
persona_1 = Persona(saldo=100.0)
persona_1.registrar()
mostrar_fecha_registro(persona_1.fecha_registro)
persona_1.cumpleaños()

print("=========================================================")

persona_2 = Persona(saldo=250.0)
persona_2.registrar()
mostrar_fecha_registro(persona_2.fecha_registro)
persona_2.cumpleaños()