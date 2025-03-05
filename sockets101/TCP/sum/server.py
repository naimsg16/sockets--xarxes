import socket


serv = socket.socket(
    family=socket.AddressFamily.AF_INET,
    type=socket.SocketKind.SOCK_STREAM,     # TCP -> STREAM 
)

serv.bind(("localhost",4320))               # we bind the socket
sum = 0
operators = 0
serv.listen(1)                              # we wait for the connections (max 1 waiting)
new_sock = serv.accept()[0]                 # we accept the connection and take the socket

while True:
    data,address = new_sock.recvfrom(10)    # we recieve the data
    int_data = int.from_bytes(data)         # we convert it into an integer
    sum += int_data                         # we add it to the total
    operators += 1                          # we count how many numbers have been passed
    if operators == 2:
        print(f'The sum is {sum}')
        break

serv.close()             
new_sock.close()                            # we close the sockets                        


