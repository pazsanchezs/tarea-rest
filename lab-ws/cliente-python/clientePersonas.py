import sys
import datetime
import configparser
import requests
from requests.structures import CaseInsensitiveDict


# Variables globales para verificación
api_personas_url_base = None
archivo_config = 'ConfigFile.properties'

def cargar_variables():
    config = configparser.RawConfigParser()
    config.read(archivo_config)

    global api_personas_url_listar, api_personas_url_crear, api_personas_url_actualizar, api_personas_url_borrar
    api_personas_url_listar = config.get('SeccionApi', 'api_personas_url_listar')
    api_personas_url_crear = config.get('SeccionApi', 'api_personas_url_crear')
    api_personas_url_actualizar = config.get('SeccionApi', 'api_personas_url_actualizar')
    api_personas_url_borrar = config.get('SeccionApi', 'api_personas_url_borrar')


def listar():
    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Content-Type"] = "application/json"

    datos = { }
    
    
    r = requests.get(api_personas_url_listar, headers=headers, json=datos)
    if (r.status_code == 200):
        # Validar response
        listado = r.json()
        for item in listado:
            print( "      " + str(item) )
    else:
        print( "Error " + str(r.status_code))


def crear(cedula: int, nombre: str, apellido: str):
    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Content-Type"] = "application/json"

    datos = {'cedula': cedula, 
             'nombre' : nombre,
             'apellido' : apellido
            }
    
    r = requests.post(api_personas_url_crear, headers=headers, json=datos)
    if (r.status_code >= 200 and r.status_code < 300):
        # Validar response
        print(r)
        
    else:
        print( "Error " + str(r.status_code))
        print(str(r.json()))


def actualizar(cedula: int, nombre: str, apellido: str):
    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Content-Type"] = "application/json"

    datos = {'nombre': nombre, 'apellido': apellido}
    url = api_personas_url_actualizar.format(cedula=cedula)

    r = requests.put(url, headers=headers, json=datos)
    if r.status_code >= 200 and r.status_code < 300:
        print("Persona actualizada:", r.json())
    else:
        print("Error " + str(r.status_code))
        print(str(r.json()))

def borrar(cedula: int):
    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Content-Type"] = "application/json"

    url = api_personas_url_borrar.format(cedula=cedula)
    r = requests.delete(url, headers=headers) 
    if r.status_code == 200: 
        print("Persona borrada con éxito.")
    else:
        print("Error al borrar la persona " + str(r.status_code))


#######################################################
######  Procesamiento principal
#######################################################
print("Iniciando " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
cargar_variables()

print("Primer listado de personas:")
listar()
print("________________")

#Crear persona
print("Crear nueva persona:")
cedula = int(input("Ingrese cedula: "))
nombre = input("Ingrese nombre: ")
apellido = input("Ingrese apellido: ")
crear(cedula, nombre, apellido)

print("________________")
print("Segundo listado de personas:")
listar()

# Actualizar persona
print("Actualizar persona:")
cedula_actualizar = int(input("Ingrese cédula de la persona a actualizar: "))
nombre_actualizar = input("Ingrese nuevo nombre: ")
apellido_actualizar = input("Ingrese nuevo apellido: ")
actualizar(cedula_actualizar, nombre_actualizar, apellido_actualizar)

print("________________")
print("Listado de personas después de la actualización:")
listar()

# Borrar persona
print("Borrar persona:")
cedula_borrar = int(input("Ingrese cédula de la persona a borrar: "))
borrar(cedula_borrar)

print("________________")
print("Listado final de personas:")
listar()

print("Finalizando " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
