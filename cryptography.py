#ENCRIPTACION DE LA BASE DE DATOS

from cryptography.fernet import Fernet
#pip install cryptography

def generar_clave():
    clave = Fernet.generate_key()
    with open("clave.key", "wb") as archivo_clave:
        archivo_clave.write(clave)
generar_clave()

def cargar_clave():
    return open("clave.key","rb").read()

#encriptacion
def encriptar_datos(dato):
    clave=cargar_clave()
    fernet=Fernet(clave)
    return fernet.encrypt(dato.encode())

#desencriptacion
def desencriptar_datos(dato_encriptado):
    clave=cargar_clave()
    fernet=Fernet(clave)
    return fernet.decrypt(dato_encriptado).decode()