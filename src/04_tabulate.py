
# Modulos que se utilizaran
import os
import requests
from dotenv import load_dotenv
from tabulate import tabulate

# Cargar las credenciales del archivo .env
load_dotenv()

baseUri = os.getenv(
    "CONTROLLER_URL",
    "http://localhost:58000"
).rstrip("/") + "/api/v1"

# 1. Solicitar el ticket de autenticacion
data = {
    "username": os.getenv("CONTROLLER_USERNAME"),
    "password": os.getenv("CONTROLLER_PASSWORD")
}

resp = requests.post(baseUri + "/ticket", json=data)

print("Estado de autenticacion:", resp.status_code)
resp.raise_for_status()

ticket = resp.json()["response"]["serviceTicket"]
print("Autenticacion exitosa.")

# 2. Consultar los dispositivos de red
headers = {"X-Auth-Token": ticket}

resp = requests.get(
    baseUri + "/network-device",
    headers=headers
)
resp.raise_for_status()

print("\nDispositivos de Red:")

host_list = []

for i, item in enumerate(resp.json()["response"], start=1):
    host_list.append([
        i,
        item.get("hostname"),
        item.get("serialNumber"),
        item.get("softwareVersion")
    ])

print(tabulate(
    host_list,
    headers=["Nro.", "Hostname", "Serial Number", "Software Version"],
    tablefmt="rst"
))

# 3. Consultar los hosts
resp = requests.get(
    baseUri + "/host",
    headers=headers
)
resp.raise_for_status()

print("\nHosts de la Red:")

host_list = []

for i, item in enumerate(resp.json()["response"], start=1):
    host_list.append([
        i,
        item.get("hostName"),
        item.get("hostType"),
        item.get("hostIp")
    ])

print(tabulate(
    host_list,
    headers=["Nro.", "Hostname", "Tipo", "IP"],
    tablefmt="rst"
))
