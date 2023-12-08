import socket
host="127.0.0.1"
port=6500
s=socket.socket()
s.bind((host,port))
s.listen()
data,add=s.accept()
while True:
    msg=data.recv(1024)
    z=msg.decode('ascii')
    print(z)
    response=input("response message:")
    send=response.encode('ascii')
    data.send(send)