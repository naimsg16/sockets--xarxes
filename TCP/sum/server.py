import socket
import time


serv = socket.socket(
    family=socket.AddressFamily.AF_INET,
    type=socket.SocketKind.SOCK_STREAM,   
)

serv.bind(("localhost",4320))
#time.sleep(15)
sum = 0
operators = 0
serv.listen(1)
new_sock = serv.accept()[0]

while True:
    data,address = new_sock.recvfrom(10)
    int_data = int.from_bytes(data)
    sum += int_data
    operators += 1
    if operators == 2:
        print(f'The sum is {sum}')
        break

serv.close()
new_sock.close()


