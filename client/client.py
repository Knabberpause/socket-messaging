import socket

connected = False
while connected == False:
    hostaddress = input('enter [server ip] or [local]')
    if hostaddress == 'local':
        try:
            host = socket.gethostname()
        except:
            print('could not get hostname')
    else:
        host = hostaddress
        print(f'host: {host}')

    port = 5000
    try:
        client_socket = socket.socket() 
        client_socket.connect((host, port))
        connected = True
    except socket.gaierror:
        print('cannot connect to server')

message = input("msg->") 


client_socket.send(message.encode()) 
data = client_socket.recv(2048).decode()

print('                    ' + data)

message = input(" msg-> ")

while message.lower().strip() != 'bye':
    client_socket.send(message.encode()) 
    data = client_socket.recv(1024).decode() 

    print('                    ' + data)

    message = input(" msg-> ") 

    break
client_socket.send('connection closed'.encode())
quit()