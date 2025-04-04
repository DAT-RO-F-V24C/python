from socket import *

serverName = 'localhost'
serverPort = 12000

msg = input('Input lowercase sentence: ')

csocket = socket(AF_INET, SOCK_DGRAM)
csocket.sendto(msg.encode(), (serverName,serverPort))
returnMsg, serverAdr = csocket.recvfrom(3000)
returnMsg = returnMsg.decode()

print(f'From server : {returnMsg}')
csocket.close()
