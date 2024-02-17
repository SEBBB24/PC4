def guardar_tabla_multiplicar(numero):
    try:
        with open(f"tabla-{numero}.txt", "w") as archivo:
            for i in range(1, 11):
                archivo.write(f"{numero} x {i} = {numero * i}\n")
        print(f"Tabla de multiplicar del {numero} guardada en tabla-{numero}.txt")
    except Exception as e:
        print(f"Error al guardar la tabla de multiplicar: {e}")

def mostrar_tabla_multiplicar(numero):
    try:
        with open(f"tabla-{numero}.txt", "r") as archivo:
            tabla = archivo.read()
        print(f"Tabla de multiplicar del {numero}:\n{tabla}")
    except FileNotFoundError:
        print(f"El archivo tabla-{numero}.txt no existe.")
    except Exception as e:
        print(f"Error al leer la tabla de multiplicar: {e}")

def mostrar_linea_tabla_multiplicar(numero, linea):
    try:
        with open(f"tabla-{numero}.txt", "r") as archivo:
            lineas = archivo.readlines()
        if 1 <= linea <= len(lineas):
            print(f"Línea {linea}: {lineas[linea - 1].strip()}")
        else:
            print(f"La línea {linea} no existe en la tabla de multiplicar del {numero}.")
    except FileNotFoundError:
        print(f"El archivo tabla-{numero}.txt no existe.")
    except Exception as e:
        print(f"Error al leer la línea de la tabla de multiplicar: {e}")

def main():
    while True:
        print("\nMENU:")
        print("1. Guardar tabla de multiplicar")
        print("2. Mostrar tabla de multiplicar")
        print("3. Mostrar línea de la tabla de multiplicar")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            numero = int(input("Ingrese un número entero entre 1 y 10: "))
            if 1 <= numero <= 10:
                guardar_tabla_multiplicar(numero)
            else:
                print("Número fuera de rango. Debe estar entre 1 y 10.")
        elif opcion == "2":
            numero = int(input("Ingrese un número entero entre 1 y 10: "))
            if 1 <= numero <= 10:
                mostrar_tabla_multiplicar(numero)
            else:
                print("Número fuera de rango. Debe estar entre 1 y 10.")
        elif opcion == "3":
            numero = int(input("Ingrese un número entero entre 1 y 10: "))
            linea = int(input("Ingrese el número de línea que desea mostrar: "))
            if 1 <= numero <= 10:
                mostrar_linea_tabla_multiplicar(numero, linea)
            else:
                print("Número fuera de rango. Debe estar entre 1 y 10.")
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()

