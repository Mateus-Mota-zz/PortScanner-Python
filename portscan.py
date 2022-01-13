import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.settimeout(0.05)

ip = input('Digite o Host a ser verificado: ')
port = int(input('Digite a Porta a ser verificado: '))

code = client.connect_ex((ip, port))


if code == 0:
    print('Porta Aberta')
else:
    print('Porta fechada')