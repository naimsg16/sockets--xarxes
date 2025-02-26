import socket
import time

serv_address = ("localhost",4320)

cli = socket.socket(
    family=socket.AddressFamily.AF_INET,
    type=socket.SocketKind.SOCK_DGRAM,      # UDP -> DGRAM  
)

cli.bind(("localhost",4222))
time.sleep(5)

cli.sendto(int.to_bytes(5),serv_address) 
cli.close()