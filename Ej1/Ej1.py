import requests

def obtener_precio_bitcoin():
    try:
        respuesta = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        respuesta.raise_for_status()
        return float(respuesta.json()['bpi']['USD']['rate'].replace(',', '')) #string a float
    except (requests.RequestException, KeyError, ValueError) as e:
        print(f"Error: {e}")
        return None

def main():
    try:
        bitcoins = float(input("Ingrese la cantidad de bitcoins que posee: "))
    except ValueError:
        print("Ingrese un número válido de bitcoins.")
        return
    
    precio_bitcoin = obtener_precio_bitcoin()
    if precio_bitcoin is not None:
        costo_en_usd = bitcoins * precio_bitcoin
        print(f"El costo actual de {bitcoins:,.4f} Bitcoins es ${costo_en_usd:,.4f} USD.")

if __name__ == "__main__":
    main()

