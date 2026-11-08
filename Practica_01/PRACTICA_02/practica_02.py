"""
2. Crear un entorno virtual y aplicar lo siguiente:
- Caso: Reporte de calificaciones:
Se tiene un alumno con calificaciones en tres cursos:
Matemáticas: 17, Ciencia: 14, Historia: 15
Cada curso tiene un peso diferente en la nota final:
Matemáticas: 40%, Ciencia: 30%, Historia: 30%
Realizar lo que se pide a continuación:
Calcula la nota final ponderada del alumno.
Muestra un mensaje como: "La nota final es: 15.6" con 1 decimal.
Evalúa si el alumno aprueba (nota final >= 13.0). Muestra un mensaje booleano:
"¿Aprobado?: True" o "¿Aprobado?: Sí"
Genera una cadena resumen que diga:
"El estudiante obtuvo una nota final de 15.6 y su estado final es: Aprobado"
En caso no apruebe indicar lo contrario en los mensajes.
"""
matematicas = 17
ciencia = 14
historia = 15

nota_final = (matematicas * 0.40) + (ciencia * 0.30) + (historia * 0.30)

print(f"La nota final es: {nota_final:.1f}")

aprobado = nota_final >= 13.0
print(f"¿Aprobado?: {aprobado}")

if aprobado:
    estado = "Aprobado"
else:
    estado = "No aprobado"

resumen = f"El estudiante obtuvo una nota final de {nota_final:.1f} y su estado final es: {estado}"
print(resumen)