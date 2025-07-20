from cryptography.fernet import Fernet
import os

def generar_clave(nombre_archivo_clave="clave.key"):
    clave = Fernet.generate_key()
    with open(nombre_archivo_clave, 'wb') as archivo_clave:
        archivo_clave.write(clave)
    print("Clave privada generada y guardada.")

def cargar_clave(nombre_archivo_clave="clave.key"):
    with open(nombre_archivo_clave, 'rb') as archivo_clave:
        return archivo_clave.read()

def crear_archivo_datos(nombre_archivo="datos_cliente.txt"):
    datos = """Nombre: Juan Perez
Numero de cuenta: 123456789
Saldo: $10.000.000
Transacciones recientes: 
 - Pago Tarjeta Credito: $500.000
 - Transferencia recibida: $2.000.000"""
    with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
        archivo.write(datos)
    print("Archivo de datos del cliente creado.")

def cifrar_archivo(nombre_archivo, clave, nombre_archivo_cifrado):
    f = Fernet(clave)
    with open(nombre_archivo, 'rb') as archivo:
        datos = archivo.read()
    datos_cifrados = f.encrypt(datos)
    with open(nombre_archivo_cifrado, 'wb') as archivo_cifrado:
        archivo_cifrado.write(datos_cifrados)
    print("Archivo cifrado guardado como:", nombre_archivo_cifrado)

def descifrar_archivo(nombre_archivo_cifrado, clave):
    f = Fernet(clave)
    with open(nombre_archivo_cifrado, 'rb') as archivo_cifrado:
        datos_cifrados = archivo_cifrado.read()
    datos_descifrados = f.decrypt(datos_cifrados)
    print("\nDatos descifrados:\n")
    print(datos_descifrados.decode('utf-8'))

def simulacion_proteccion_datos_cliente():
    generar_clave()
    clave = cargar_clave()

    nombre_original = "datos_cliente.txt"
    nombre_cifrado = "datos_cliente_cifrado.txt"

    crear_archivo_datos(nombre_original)
    cifrar_archivo(nombre_original, clave, nombre_cifrado)

    print("\nSimulando transmision segura...\n")

    descifrar_archivo(nombre_cifrado, clave)

    # os.remove(nombre_original)
    # os.remove(nombre_cifrado)
    # os.remove("clave.key")

simulacion_proteccion_datos_cliente()
