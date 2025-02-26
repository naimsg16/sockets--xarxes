import socket
import time

serv_address = ("localhost",4320)

cli = socket.socket(
    family=socket.AddressFamily.AF_INET,
    type=socket.SocketKind.SOCK_STREAM,   
)
# UDP = DGRAM, TCP = STREAM

cli.bind(("localhost",4222)) # se puede ignorar
time.sleep(5)

cli.connect(serv_address)
cli.sendto(int.to_bytes(6),serv_address)
cli.sendto(int.to_bytes(7),serv_address)

cli.close()