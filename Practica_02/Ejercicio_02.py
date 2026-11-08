class Persona:
    nacionalidad = "Peruana"

    def __init__(self, nombre, edad, saldo):
        self.nombre = nombre
        self.edad = edad
        self.saldo = saldo

    def consultar_saldo(self):
        print("Saldo actual de {}: S/ {:.2f}".format(self.nombre, self.saldo))

    def transferir(self, otra_persona):
        while True:
            try:
                monto = float(
                    input("\nIngrese el monto que {} transferirá a {}: ".format(self.nombre, otra_persona.nombre)))

                if monto <= 0:
                    print("Error: El monto debe ser mayor a cero.")
                elif monto > self.saldo:
                    print("Error: Saldo insuficiente.")
                    print("Disponible: S/ {:.2f}".format(self.saldo))
                    # Informa y conserva los saldos sin cambios
                    break
                else:
                    self.saldo -= monto
                    otra_persona.saldo += monto
                    print("Transferencia realizada correctamente.")
                    break

            except ValueError:
                print("Error: debe ingresar un valor numérico.")


# Pruebas Ejercicio 2
persona_A = Persona("George", 13, 500.0)
persona_B = Persona("Peppa", 15, 150.0)

persona_A.consultar_saldo()
persona_B.consultar_saldo()

print("\n--- Intento de transferencia rechazada ---")
persona_A.transferir(persona_B)

print("\n--- Intento de transferencia válida ---")
persona_A.transferir(persona_B)

print("\n--- Saldos Finales ---")
persona_A.consultar_saldo()
persona_B.consultar_saldo()