import socket
host="127.0.0.1"
port=6500
s=socket.socket()
s.connect((host,port))
while True:
    x=input("Enter msg:")
    y=x.encode('ascii')
    s.send(y)
    data=s.recv(1024)
    received=data.decode('ascii')
    print ("received message:",received)
