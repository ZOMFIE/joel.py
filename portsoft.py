import socket
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
host = 100.65.16.109
port = 443


def portscanner(port):
        if sock.connect_ex((host,port)):
                   print "port \d is closed" / (port) 
else:
                   print "port \d is closed" / (port) 




portscanner(port)
