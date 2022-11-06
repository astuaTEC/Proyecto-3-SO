# Importamos Fernet
from cryptography.fernet import Fernet

#https://pythondiario.com/2018/09/cryptography-cifrado-simetrico.html

if __name__ == "__main__":
    # Generamos una clave
    clave = Fernet.generate_key()

    # Creamos la instancia de Fernet
    # Parametros: key: clave generada
    f = Fernet(clave)

    # Encriptamos el mensaje
    # utilizando el método "encrypt"
    token = f.encrypt(b'Mensaje secreto')

    # Mostramos el token del mensaje
    print(token)
    print("Clave ", clave)