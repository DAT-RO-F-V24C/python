import socket

ServerName = 'localhost'
ServerPort = 7

csocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
csocket.connect((ServerName,ServerPort))

sentence = input('Skrev din linje du vil sende')

csocket.send(sentence.encode())
svarLinje = csocket.recv(1024)
#print(svarLinje)
linjeSomTekst = svarLinje.decode()

print(linjeSomTekst)

csocket.close()


