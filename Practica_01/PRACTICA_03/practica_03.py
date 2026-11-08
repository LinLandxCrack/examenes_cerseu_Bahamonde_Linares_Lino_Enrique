"""
3. Generar un nuevo entorno virtual
- Caso: Calculadora de propinas
Crea un programa que permita ingresar el total de una cuenta en un restaurante,
el porcentaje de propina que desea dejar el cliente y el número de personas que
dividirán la cuenta. El programa debe mostrar:
El monto total con propina.
El monto que debe pagar cada persona (con 2 decimales).
Un mensaje será personalizado, indicará si el monto individual supera los 100
soles, mostrando un mensaje de advertencia si es el caso.
"""
total_cuenta = 200.0
porcentaje_propina = 15.0
numero_personas = 2

monto_propina = total_cuenta * (porcentaje_propina / 100)
monto_total = total_cuenta + monto_propina
monto_por_persona = monto_total / numero_personas

print(f"Monto total con propina: S/. {monto_total:.2f}")
print(f"Cada persona debe pagar: S/. {monto_por_persona:.2f}")

if monto_por_persona > 100:
    print("¡Advertencia! El monto por persona supera los S/. 100")