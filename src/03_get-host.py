
import os
import requests
from dotenv import load_dotenv

# Cargar las credenciales desde .env
load_dotenv()

controller_url = os.getenv(
    "CONTROLLER_URL",
    "http://localhost:58000"
).rstrip("/")

username = os.getenv("CONTROLLER_USERNAME")
password = os.getenv("CONTROLLER_PASSWORD")

# 1. Obtener un ticket de autenticación
ticket_url = controller_url + "/api/v1/ticket"

body_json = {
    "username": username,
    "password": password
}

ticket_response = requests.post(ticket_url, json=body_json)
ticket_response.raise_for_status()

service_ticket = ticket_response.json()["response"]["serviceTicket"]

print("Autenticación exitosa.")

# 2. Consultar los hosts
api_url = controller_url + "/api/v1/host"

headers = {
    "X-Auth-Token": service_ticket
}

resp = requests.get(api_url, headers=headers)

print("Request status:", resp.status_code)
resp.raise_for_status()

response_json = resp.json()
hosts = response_json["response"]

# 3. Mostrar los hosts encontrados
print()
print("HOSTS DE LA RED")
print("------------------")

for host in hosts:
    print(
        host.get("hostName"),
        "\t",
        host.get("hostIp"),
        "\t",
        host.get("hostMac"),
        "\t",
        host.get("connectedInterfaceName")
    )

print("------------------")
print("Total de hosts:", len(hosts))
