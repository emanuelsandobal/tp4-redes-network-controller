
import os
import requests
from dotenv import load_dotenv

# Cargar la configuración privada
load_dotenv()

url = os.getenv("CONTROLLER_URL")
usuario = os.getenv("CONTROLLER_USERNAME")
contrasena = os.getenv("CONTROLLER_PASSWORD")

if not all([url, usuario, contrasena]):
    raise SystemExit("Error: faltan variables en el archivo .env")

url = url.rstrip("/")

try:
    # 1. Solicitar un ticket de autenticación
    respuesta = requests.post(
        f"{url}/api/v1/ticket",
        json={
            "username": usuario,
            "password": contrasena
        },
        timeout=10
    )
    respuesta.raise_for_status()

    ticket = respuesta.json()["response"]["serviceTicket"]

    print("Autenticación exitosa.")

    # 2. Consultar el inventario de dispositivos
    respuesta = requests.get(
        f"{url}/api/v1/network-device",
        headers={"X-Auth-Token": ticket},
        timeout=15
    )
    respuesta.raise_for_status()

    dispositivos = respuesta.json().get("response", [])

    print("\nINVENTARIO DE DISPOSITIVOS")
    print("--------------------------")

    for dispositivo in dispositivos:
        print("Nombre:", dispositivo.get("hostname", "Sin nombre"))
        print("IP:", dispositivo.get("managementIpAddress", "Sin IP"))
        print("Tipo:", dispositivo.get("type", "No especificado"))
        print("--------------------------")

    print(f"Total de dispositivos: {len(dispositivos)}")

except requests.exceptions.RequestException as error:
    print("Error de comunicación con el controlador:")
    print(error)

except (KeyError, TypeError, ValueError) as error:
    print("Error al interpretar la respuesta de la API:")
    print(error)
