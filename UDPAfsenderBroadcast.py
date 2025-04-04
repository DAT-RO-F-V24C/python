from socket import *
import time

serverName = '255.255.255.255' #broadcast adresse på subnettet
serverPort = 17000

msg = input('Input lowercase sentence: ')

csocket = socket(AF_INET, SOCK_DGRAM)
csocket.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

for i in range(10):
    csocket.sendto(msg.encode(), (serverName,serverPort))
    time.sleep(10)

csocket.close()