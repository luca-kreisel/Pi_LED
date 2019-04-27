import socket


#Create and bind socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#So you can reuse server after restart more quickly
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(("",6000))

s.listen(1)

while True:
    s_new, client = s.accept()
    print (client)
    while True:
        data_recv = s_new.recv(34)

        data = data_recv.decode(encoding="utf-8")
        print (data)

