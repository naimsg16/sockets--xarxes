import socket
import time


serv = socket.socket(
    family=socket.AddressFamily.AF_INET,
    type=socket.SocketKind.SOCK_DGRAM,   
)

serv.bind(("localhost",4320))
#serv.listen(2)
time.sleep(10)
sum = 0
operators = 0
while True:
    data,client_addr = serv.recvfrom(10)
    int_data = int.from_bytes(data)
    operators += 1
    sum += int.from_bytes(data)
    if operators == 2:
        print(f"The sum is {sum}")
        serv.close()
        break
        

