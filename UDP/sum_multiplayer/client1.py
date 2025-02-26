import socket
import time

cli = socket.socket(
    family=socket.AddressFamily.AF_INET,
    type=socket.SocketKind.SOCK_DGRAM,   
)
# UDP = DGRAM, TCP = STREAM

cli.bind(("localhost",4222)) # se puede ignorar
time.sleep(5)

cli.sendto(int.to_bytes(5),("localhost",4320)) 
cli.close()