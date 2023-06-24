import socket
import threading

connections = 0

server_socket = socket.socket()
def start_server():
    host = socket.gethostname()
    port = 5000

    server_socket.bind((host, port))
    print('server started')

    server_socket.listen(2)

def listen(conns):
    
    print("Connection from: " + str(address))
    conns +=1
    data = ''
    while True:
        try:
            data = conn.recv(2048).decode()
            if data.strip() == 'connection closed':
                print(f'from {str(address[0])}: {data}')
                print('connection closed')
                conn.close()
                break

            print(f"from {str(address[0])}: {str(data)}") 
        except ConnectionAbortedError:
            print('connection closed')
            break
        except ConnectionResetError:
            print('connection closed')
            break
        try:
            data = input(' reply: ')
            conn.send(data.encode())
        except ConnectionResetError:
            print('connection closed')
            break
        except ConnectionAbortedError:
            print('connection closed')
            break



start_server()

while True:
    conn, address = server_socket.accept()
    threading.Thread(target=listen(connections), daemon=True).start()

