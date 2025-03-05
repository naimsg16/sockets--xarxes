import socket
import time

serv_address = ("localhost",4320)

cli = socket.socket(
    family=socket.AddressFamily.AF_INET,
    type=socket.SocketKind.SOCK_STREAM,     # TCP -> STREAM
)

cli.bind(("localhost",4222))                # we bind the socket
time.sleep(5)                               # we wait in case the server is off

cli.connect(serv_address)                   # we connect to the server
cli.sendto(int.to_bytes(6),serv_address) 
cli.sendto(int.to_bytes(7),serv_address)    # we send the numbers to the server

cli.close()                                 # we close the socket