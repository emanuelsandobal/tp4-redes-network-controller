
# TP4 Integrador - Redes de Computadoras

**Universidad Nacional de La Matanza (UNLaM)**  
**Materia:** Redes de Computadoras  
**Trabajo:** TP4 Integrador

## Descripción

Este repositorio contiene programas desarrollados en Python para interactuar con la API REST del Network Controller de Cisco Packet Tracer.

El proyecto permite autenticar usuarios, consultar dispositivos de red, obtener información de los hosts y verificar el estado de conectividad de los dispositivos.

Se incluyen cuatro programas proporcionados por la cátedra, adaptados para utilizar variables de entorno, y tres programas propios.

## Programas de la cátedra (adaptados)

| Archivo | Descripción |
|---|---|
| `src/01_get-ticket.py` | Solicita un ticket de autenticación al Network Controller. |
| `src/02_get-network-device.py` | Consulta los dispositivos de red y muestra sus nombres, modelos e IP de administración. |
| `src/03_get-host.py` | Consulta los hosts y muestra nombres, direcciones IP, MAC e interfaces de conexión. |
| `src/04_tabulate.py` | Presenta los dispositivos y hosts en tablas utilizando la biblioteca `tabulate`. |

Los programas originales pertenecen a la cátedra de Redes de Computadoras y fueron obtenidos del repositorio:

https://github.com/redes-computadoras/api-python-redes-cisco

Las adaptaciones permiten utilizar credenciales mediante un archivo `.env`, sin escribir contraseñas directamente en el código.

## Programas propios

| Archivo | Descripción |
|---|---|
| `src/01_autenticacion.py` | Autentica al usuario y verifica que el Network Controller devuelva un ticket válido. |
| `src/02_inventario_dispositivos.py` | Consulta el inventario de dispositivos y muestra sus nombres, direcciones IP y tipos. |
| `src/03_estado_dispositivos.py` | Consulta el estado de conectividad de los dispositivos, indicando si están `Reachable` o `Unreachable`. |

## Requisitos

- Python.
- Cisco Packet Tracer con Network Controller configurado.
- Acceso a la API REST del controlador.
- Bibliotecas indicadas en `requirements.txt`.

## Instalación

Clonar el repositorio:

```bash
git clone https://github.com/emanuelsandobal/tp4-redes-network-controller.git
```

Entrar en la carpeta del proyecto:

```bash
cd tp4-redes-network-controller
```

Crear un entorno virtual:

```bash
python -m venv .venv
```

Activarlo en PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Instalar las dependencias:

```bash
python -m pip install -r requirements.txt
```

## Configuración

Crear un archivo `.env` en la carpeta principal del proyecto con las siguientes variables:

```env
CONTROLLER_URL=http://localhost:58000
CONTROLLER_USERNAME=TU_USUARIO
CONTROLLER_PASSWORD=TU_CONTRASENA
```

Reemplazar los valores de ejemplo por las credenciales configuradas en el Network Controller.

El archivo `.env` contiene información privada y no debe subirse a GitHub.

## Ejecución

Con el Network Controller iniciado y su API disponible, ejecutar los programas desde la carpeta principal del proyecto.

Por ejemplo:

```bash
python src/01_get-ticket.py
python src/02_get-network-device.py
python src/03_get-host.py
python src/04_tabulate.py
```

También se pueden ejecutar los programas propios:

```bash
python src/01_autenticacion.py
python src/02_inventario_dispositivos.py
python src/03_estado_dispositivos.py
```

## Endpoints utilizados

| Método | Endpoint | Función |
|---|---|---|
| POST | `/api/v1/ticket` | Obtener un ticket de autenticación. |
| GET | `/api/v1/network-device` | Consultar dispositivos de red. |
| GET | `/api/v1/host` | Consultar hosts. |

## Seguridad

Las credenciales se gestionan mediante variables de entorno utilizando `python-dotenv`.

No se incluyen contraseñas, tickets de autenticación ni archivos `.env` en el repositorio público.

## Estado del proyecto

Los siete programas fueron ejecutados y comprobados con el Network Controller de la topología del TP4 Integrador.
