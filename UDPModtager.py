from socket import *

serverPort = 12000

ssocket = socket(AF_INET, SOCK_DGRAM)
ssocket.bind(('',serverPort))
print(f'Server is ready on port {serverPort}')

while True:
    msg, clientAdr = ssocket.recvfrom(3000)
    returnMsg = msg.decode().upper()
    ssocket.sendto(returnMsg.encode(), clientAdr)
