import socket

ip = input('Digite o Host a ser verificado: ')

ports = []
count = 0

while count < 10:
    ports.append(int(input('Digite a Porta a ser verificado: ')))
    count += 1

for port in ports:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(0.05)
    code = client.connect_ex((ip, port))


    if code == 0:
        print(f'{str(port)} -> Porta Aberta')
    else:
        print(f'{str(port)} -> Porta Fechada')
        
print('Scan Finalizado')