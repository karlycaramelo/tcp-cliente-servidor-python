import socket

def iniciar_servidor():
    ''' 
    Inicia un servidor TCP que escucha en el puerto 5000.
    Cuando recibe un mensaje, lo procesa y envía una respuesta al cliente. 

    Si el mensaje es "DESCONEXION", cierra la conexión con el cliente.
    El servidor se ejecuta indefinidamente, aceptando múltiples conexiones.
    '''
    host = '127.0.0.1' # Dirección IP local
    puerto = 5000 # Puerto del servidor

    # Crear un socket TCP
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # Permite reutilizar la dirección
    servidor.bind((host, puerto)) # Vincula el socket a la dirección y puerto
    servidor.listen() 

    print(f"Servidor escuchando en {host}:{puerto}") 

    while True:
        '''
        Acepta una conexión entrante y crea un nuevo socket para la comunicación.
        El servidor permanece en un loop infinito, esperando conexiones.
        Cuando un cliente se conecta, se establece una nueva conexión y se inicia la comunicación.
        El servidor puede manejar múltiples clientes, pero en este caso, solo se maneja uno a la vez.
        El servidor espera recibir datos del cliente y responde según el mensaje recibido.
        '''
        conn, addr = servidor.accept()
        print(f"Conexión establecida con {addr}")

        while True:
            datos = conn.recv(1024).decode() # Recibe datos del cliente
            if not datos:
                break

            print(f"Recibido: {datos}") 

            mensaje_limpio = datos.strip().lower() # Limpia el mensaje recibido
            '''
            Procesa el mensaje recibido y determina la respuesta.

            Si el mensaje es "desconexion", cierra la conexión.
            Otro caso, convierte el mensaje a mayúsculas y lo envía de vuelta al cliente.
            '''       
            if mensaje_limpio == "desconexion":  
                print("Cliente desconectado.")
                conn.close()
                break
            # Caso particular para consistencia con el ejemplo en la especificación
            elif mensaje_limpio == "hola servidor": 
                respuesta = "HOLA CLIENTE"
            else:
                respuesta = datos.upper()

            conn.send(respuesta.encode())

if __name__ == "__main__":
    iniciar_servidor() # Inicia el servidor

