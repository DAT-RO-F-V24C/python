from socket import *
import RestClient
import json

#
#   get json on udp 
#   post information to KajakTur RestApi
#
serverPort = 10234

ssocket = socket(AF_INET, SOCK_DGRAM)
ssocket.bind(('',serverPort))
print(f'Server is ready on port {serverPort}')

while True:
    # receive from UDP 'broadcaster'
    msg, clientAdr = ssocket.recvfrom(3000)
    jsonStr = msg.decode()
    print(f'Modtaget json {jsonStr}')
    # forward as post-request to KajakTur API
    newKajakTur = json.loads(jsonStr)
    print(f'modtaget dict {newKajakTur}')
    RestClient.Add(newKajakTur)

    