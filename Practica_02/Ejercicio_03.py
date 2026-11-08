def solicitar_valores():
    while True:
        try:
            val1 = float(input("Ingrese el primer valor numérico: "))
            val2 = float(input("Ingrese el segundo valor numérico: "))
            return val1, val2
        except ValueError as error:
            print("Error: Ingrese solo números. Detalle: {}".format(error))

def dividir(a, b):
    try:
        resultado = a / b
    except ZeroDivisionError:
        print("Error: No se puede dividir entre cero.")
        raise
    except TypeError:
        print("Error: Tipos incompatibles para la división.")
        raise
    else:
        return resultado

def sumar(a, b):
    try:
        resultado = a + b
    except TypeError:
        print("Error: Tipos incompatibles para la suma.")
        raise
    else:
        return resultado
    finally:
        print("Bloque finally: La validación de la suma ha concluido.")

def registrar_elementos(n):
    lista = []
    for i in range(n):
        elemento = input("Ingrese el elemento {}: ".format(i + 1))
        lista.append(elemento)
    return lista

def consultar_elemento(lista, indice):
    try:
        resultado = lista[indice]
    except IndexError:
        print("Error: El índice no existe en la lista.")
        raise
    else:
        return resultado

# Pruebas Ejercicio 3
print("--- PRUEBA 1: Ingreso de datos y División ---")
while True:
    try:
        num1, num2 = solicitar_valores()
        res_div = dividir(num1, num2)
        print("Resultado de la división: {:.2f}".format(res_div))
        break
    except ZeroDivisionError:
        print("Intente nuevamente ingresando un divisor distinto de cero.\n")

print("\n--- PRUEBA 2: Suma (Implementa Else y Finally) ---")
res_suma = sumar(num1, num2)
print("Resultado de la suma: {:.2f}".format(res_suma))

print("\n--- PRUEBA 3: Registro y Consulta en Lista ---")
while True:
    try:
        cantidad = int(input("¿Cuántos elementos desea registrar?: "))
        if cantidad > 0:
            break
        print("Ingrese un número mayor a cero.")
    except ValueError:
        print("Error: Debe ingresar un número entero.")

mi_lista = registrar_elementos(cantidad)

while True:
    try:
        idx = int(input("Ingrese el índice que desea consultar (inicia en 0): "))
        item = consultar_elemento(mi_lista, idx)
        print("El elemento encontrado es: {}".format(item))
        break
    except (ValueError, IndexError):
        print("Intente nuevamente.\n")