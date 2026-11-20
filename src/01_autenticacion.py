
import os
import requests
from dotenv import load_dotenv

# Cargar las variables privadas del archivo .env
load_dotenv()

url = os.getenv("CONTROLLER_URL")
usuario = os.getenv("CONTROLLER_USERNAME")
contrasena = os.getenv("CONTROLLER_PASSWORD")

# Comprobar que estén configuradas las variables
if not all([url, usuario, contrasena]):
    raise SystemExit("Error: faltan variables en el archivo .env")

# Endpoint de autenticación del Network Controller
endpoint = f"{url.rstrip('/')}/api/v1/ticket"

# Datos que enviaremos al controlador
datos = {
    "username": usuario,
    "password": contrasena
}

try:
    respuesta = requests.post(endpoint, json=datos, timeout=10)
    respuesta.raise_for_status()

    resultado = respuesta.json()
    ticket = resultado.get("response", {}).get("serviceTicket")

    if ticket:
        print("Autenticación exitosa.")
        print("El Network Controller devolvió un ticket válido.")
    else:
        print("No se encontró el ticket en la respuesta.")

except requests.exceptions.RequestException as error:
    print("Error al comunicarse con el Network Controller:")
    print(error)
