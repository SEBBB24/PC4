import requests
from datetime import datetime

def obtener_y_guardar_precio_bitcoin():
    try:
        respuesta = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        respuesta.raise_for_status()
        precio_bitcoin = float(respuesta.json()['bpi']['USD']['rate'].replace(',', ''))  #string a float
        fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open('precios_bitcoin.txt', 'a') as archivo:
            archivo.write(f"{fecha_actual}: {precio_bitcoin:.2f} USD\n")
        print("Precio de Bitcoin guardado correctamente en el archivo.")
    except Exception as e:
        print(f"Error al obtener y guardar el precio de Bitcoin: {e}")

def main():
    obtener_y_guardar_precio_bitcoin()

if __name__ == "__main__":
    main()
