def contar_lineas_codigo(archivo):
    try:
        with open(archivo, 'r') as f:
            lineas_codigo = sum(1 for linea in f if linea.strip() and not linea.startswith("#"))
        return lineas_codigo
    except Exception as e:
        print(f"Error al leer el archivo: {e}")

def contar_lineas_codigo(archivo):
    try:
        with open(archivo, 'r') as f:
            lineas_codigo = 0
            for linea in f:
                linea = linea.strip()
                if linea and not linea.startswith("#"):
                    lineas_codigo += 1
        return lineas_codigo
    except FileNotFoundError:
        print("El archivo no existe.")
    except Exception as e:
        print(f"Error al leer el archivo: {e}")

def main():
    archivo = input("Ingrese la ruta del archivo .py: ")
    if archivo.endswith(".py"):
        lineas_codigo = contar_lineas_codigo(archivo)
        if lineas_codigo is not None:
            print(f"El número de líneas de código en el archivo {archivo} es: {lineas_codigo}")
    else:
        print("La ruta del archivo no es válida o el archivo no tiene extensión .py")

if __name__ == "__main__":
    main()
