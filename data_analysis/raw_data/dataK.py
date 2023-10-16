import requests
import json
import time

# URL del archivo JSON que deseas descargar
url = "https://services.swpc.noaa.gov/products/noaa-planetary-k-index.json"

# Directorio donde guardar los archivos JSON descargados
output_directory = "data/"

# Intervalo de tiempo en segundos (un día)
intervalo_tiempo_segundos = 24 * 60 * 60  # 24 horas * 60 minutos * 60 segundos

while True:
    try:
        # Realiza la solicitud GET para obtener el contenido JSON
        response = requests.get(url)

        # Verifica si la solicitud fue exitosa
        if response.status_code == 200:
            # Lee el contenido JSON
            data = response.json()

            # Genera un nombre de archivo único basado en la fecha y la hora
            timestamp = time.strftime("%Y%m%d-%H%M%S")
            file_name = f"noaa-planetary-k-index_{timestamp}.json"

            # Define la ruta completa para guardar el archivo
            output_file_path = output_directory + file_name

            # Guarda el contenido JSON en un archivo
            with open(output_file_path, "w") as output_file:
                json.dump(data, output_file, indent=4)

            print(f"Archivo '{file_name}' descargado y guardado con éxito en '{output_file_path}'")
        else:
            print(f"Error al descargar el archivo: Código de estado {response.status_code}")

        # Espera el intervalo de tiempo antes de la próxima descarga (un día)
        time.sleep(intervalo_tiempo_segundos)

    except Exception as e:
        print(f"Error al descargar el archivo: {str(e)}")

