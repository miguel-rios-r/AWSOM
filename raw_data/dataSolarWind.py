import requests
import json
import time

# Lista de archivos JSON que deseas descargar
files_to_download = [
    "mag-1-day.json",
    "mag-3-day.json",
    "plasma-1-day.json",
    "plasma-3-day.json"
]

# URL base de la NOAA
base_url = "https://services.swpc.noaa.gov/products/solar-wind/"

# Directorio donde guardar los archivos JSON descargados
output_directory = "data/"

# Loop para descargar los archivos
for file_name in files_to_download:
    # Construye la URL completa
    file_url = base_url + file_name

    try:
        # Realiza la solicitud GET para obtener el contenido JSON
        response = requests.get(file_url)

        # Verifica si la solicitud fue exitosa
        if response.status_code == 200:
            # Lee el contenido JSON
            data = response.json()

            # Define la ruta completa para guardar el archivo
            output_file_path = output_directory + file_name

            # Guarda el contenido JSON en un archivo
            with open(output_file_path, "w") as output_file:
                json.dump(data, output_file, indent=4)

            print(f"Archivo '{file_name}' descargado y guardado con éxito en '{output_file_path}'")
        else:
            print(f"Error al descargar el archivo '{file_name}': Código de estado {response.status_code}")
        
        # Espera 1 segundo antes de la próxima descarga para evitar sobrecargar el servidor
        time.sleep(1)

    except Exception as e:
        print(f"Error al descargar el archivo '{file_name}': {str(e)}")

print("Descarga de archivos completada.")
