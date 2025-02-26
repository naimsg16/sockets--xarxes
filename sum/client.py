import socket
import time

cli = socket.socket(
    family=socket.AddressFamily.AF_INET,
    type=socket.SocketKind.SOCK_DGRAM,   
)
# UDP = DGRAM, TCP = STREAM

cli.bind(("localhost",4222)) # se puede ignorar

number = int(input('Enter a number to sum: '))

while True:
    cli.sendto(int.to_bytes(number),("localhost",4320)) 
    if number == 0:
        break
    number = int(input('Enter a number to sum: '))

cli.close()