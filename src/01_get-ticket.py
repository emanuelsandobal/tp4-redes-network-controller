import json
import os
import requests
from dotenv import load_dotenv

# Cargar las variables del archivo .env
load_dotenv()

api_url = os.getenv("CONTROLLER_URL", "http://localhost:58000").rstrip("/") + "/api/v1/ticket"

headers = {
    "content-type": "application/json"
}

body_json = {
    "username": os.getenv("CONTROLLER_USERNAME"),
    "password": os.getenv("CONTROLLER_PASSWORD")
}

resp = requests.post(api_url, json.dumps(body_json), headers=headers)

print("Ticket request status:", resp.status_code)

response_json = resp.json()

if resp.status_code in (200, 201):
    serviceTicket = response_json["response"]["serviceTicket"]
    print("Autenticación exitosa.")
    print("El Network Controller devolvió un ticket válido.")
else:
    print("Error de autenticación:")
    print(response_json)