import requests
import json

url = "https://services.swpc.noaa.gov/products/noaa-planetary-k-index.json"

try:
    # Realiza una solicitud GET a la URL
    response = requests.get(url)

    # Verifica si la solicitud fue exitosa (código de estado 200)
    if response.status_code == 200:
        # Analiza el contenido JSON
        data = json.loads(response.text)
        
        # Ahora puedes trabajar con 'data' como un diccionario
        print(data)
    else:
        print(f"Error al obtener la URL. Código de estado: {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"Error de solicitud: {e}")
except json.JSONDecodeError as e:
    print(f"Error al analizar JSON: {e}")