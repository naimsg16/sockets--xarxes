import socket

serv_address = ("localhost",4320)

cli = socket.socket(
    family=socket.AddressFamily.AF_INET,
    type=socket.SocketKind.SOCK_DGRAM,              # UDP -> DGRAM
)

cli.bind(("localhost",4222))

number = int(input('Enter a number: '))             

while True:
    cli.sendto(int.to_bytes(number),serv_address) 
    if number == 0:
        break
    number = int(input('Enter a number: '))

cli.close()