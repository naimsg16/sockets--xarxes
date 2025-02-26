import socket
import time

serv = socket.socket(
    family=socket.AddressFamily.AF_INET,
    type=socket.SocketKind.SOCK_STREAM,   
)

serv.bind(("localhost",4320))
serv.listen(2)
time.sleep(15)
serv.accept()
serv.accept()

sum = 0
operators = 0
while True:
    data,client_addr = serv.recvfrom(10)
    int_data = int.from_bytes(data)
    sum += int.from_bytes(data)
    operators += 1
    if operators == 2:
        print(f"The sum is {sum}")
        serv.close()
        break


        