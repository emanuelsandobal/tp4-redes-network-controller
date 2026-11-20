import os
import requests
from dotenv import load_dotenv

# Cargar las credenciales privadas
load_dotenv()

url = os.getenv("CONTROLLER_URL")
usuario = os.getenv("CONTROLLER_USERNAME")
contrasena = os.getenv("CONTROLLER_PASSWORD")

if not all([url, usuario, contrasena]):
    raise SystemExit("Error: faltan variables en el archivo .env")

url = url.rstrip("/")

try:
    # 1. Autenticarse en el Network Controller
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

    # 2. Consultar los dispositivos
    respuesta = requests.get(
        f"{url}/api/v1/network-device",
        headers={"X-Auth-Token": ticket},
        timeout=15
    )
    respuesta.raise_for_status()

    dispositivos = respuesta.json().get("response", [])

    # 3. Mostrar el estado de cada dispositivo
    print("\nESTADO DE LOS DISPOSITIVOS")
    print("--------------------------")

    for dispositivo in dispositivos:
        nombre = dispositivo.get("hostname") or "Sin nombre"
        ip = dispositivo.get("managementIpAddress") or "Sin IP"
        estado = dispositivo.get("reachabilityStatus", "No informado")

        print(f"Dispositivo: {nombre}")
        print(f"IP: {ip}")
        print(f"Estado: {estado}")
        print("--------------------------")

    print(f"Total de dispositivos: {len(dispositivos)}")

except requests.exceptions.RequestException as error:
    print("Error de comunicación con el controlador:")
    print(error)

except (KeyError, TypeError, ValueError) as error:
    print("Error al interpretar la respuesta de la API:")
    print(error)