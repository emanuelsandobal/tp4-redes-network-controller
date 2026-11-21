
import os
import requests
from dotenv import load_dotenv

# Cargar las credenciales del archivo .env
load_dotenv()

controller_url = os.getenv(
    "CONTROLLER_URL",
    "http://localhost:58000"
).rstrip("/")

username = os.getenv("CONTROLLER_USERNAME")
password = os.getenv("CONTROLLER_PASSWORD")

# 1. Solicitar un ticket de autenticación
ticket_url = controller_url + "/api/v1/ticket"

body_json = {
    "username": username,
    "password": password
}

ticket_response = requests.post(ticket_url, json=body_json)
ticket_response.raise_for_status()

service_ticket = ticket_response.json()["response"]["serviceTicket"]

print("Autenticación exitosa.")

# 2. Consultar los dispositivos de red
api_url = controller_url + "/api/v1/network-device"

headers = {
    "X-Auth-Token": service_ticket
}

resp = requests.get(api_url, headers=headers)

print("Request status:", resp.status_code)
resp.raise_for_status()

response_json = resp.json()
networkDevices = response_json["response"]

# 3. Mostrar los dispositivos
print()
print("DISPOSITIVOS DE RED")
print("------------------")

for networkDevice in networkDevices:
    print(
        networkDevice.get("hostname"),
        "\t",
        networkDevice.get("platformId"),
        "\t",
        networkDevice.get("managementIpAddress")
    )
