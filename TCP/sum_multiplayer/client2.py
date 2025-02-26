import socket
import time

serv_address = ("localhost",4320)

cli = socket.socket(
    family=socket.AddressFamily.AF_INET,
    type=socket.SocketKind.SOCK_STREAM,     # TCP -> STREAM 
)

cli.bind(("localhost",4223))
time.sleep(5)

cli.connect(serv_address)

cli.sendto(int.to_bytes(6),serv_address) 
cli.close()