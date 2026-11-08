"""
4. Registro de participantes con listas
Crea una lista vacía y realiza lo siguiente:
Agrega los nombres de tres participantes.
Inserta un nuevo participante en la segunda posición.
Actualiza el nombre del primer participante.
Elimina uno de los participantes.
Muestra la lista final y la cantidad de participantes registrados.
No utilizar ciclos ni recorridos.
"""

participantes = []

participantes.append("Marcelo")
participantes.append("Maria")
participantes.append("Pedro")

participantes.insert(1, "Luis")

participantes[0] = "Carlos"

participantes.remove("Maria")
print("Lista final de participantes:", participantes)

print("Lista final de participantes:", participantes)
print("Cantidad de participantes:", len(participantes))