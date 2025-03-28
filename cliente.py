import socket

def iniciar_cliente():
    '''
    Inicia un cliente TCP que se conecta a un servidor en el puerto 5000.
    Envía mensajes al servidor y recibe respuestas.
    '''
    host = '127.0.0.1' 
    puerto = 5000

    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Crear un socket TCP para el cliente
    cliente.connect((host, puerto)) # Conecta al servidor

    while True:
        '''
        Envía un mensaje al servidor y espera una respuesta.
        '''
        mensaje = input("Escribe un mensaje (o DESCONEXION para salir): ")
        cliente.send(mensaje.encode())

        if mensaje.strip().upper() == "DESCONEXION":
            break

        respuesta = cliente.recv(1024).decode()
        print(f"Respuesta del servidor: {respuesta}") # Imprime la respuesta del servidor

    cliente.close() # Cierra la conexión
    print("Conexión cerrada.")

if __name__ == "__main__":
    iniciar_cliente() # Inicia el cliente
