from pyfiglet import Figlet
import random

def solicitar_fuente():
    figlet = Figlet()
    fuentes_disponibles = figlet.getFonts()
    fuente = input("Ingrese el nombre de la fuente (o presione Enter para seleccionar una aleatoria):\n")
    if fuente.strip() == "":
        fuente = random.choice(fuentes_disponibles)
        print(f"Fuente seleccionada aleatoriamente: {fuente}")
    return fuente

def solicitar_texto():
    return input("Ingrese el texto a mostrar: ")

def imprimir_texto_con_fuente(texto, fuente):
    figlet = Figlet(font=fuente)
    texto_renderizado = figlet.renderText(texto)
    print(texto_renderizado)

def main():
    fuente = solicitar_fuente()
    texto = solicitar_texto()
    imprimir_texto_con_fuente(texto, fuente)

if __name__ == "__main__":
    main()

