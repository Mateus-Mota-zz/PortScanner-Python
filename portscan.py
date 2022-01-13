import socket
import nmap

scanner = nmap.PortScanner()

print("Seja bem-vindo ao PortScanner")
print("-----------------------------")

ip = input('Digite o IP a ser varrido: ')

menu = input("""\n Escolha o tipo de varredura a ser realizada
                1 -> Varredura do tipo SYN
                2 -> Varredura do tipo UDP
                3 -> Varredura do tipo Intensa
                Digite a opção escolhida: """)
print(f"A opção escolhida foi: {menu}")

ports = []
count = 0

while count < 5:
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

if menu == "1":
    print(f'Versão do nMAP: {scanner.nmap_version()}')
    scanner.scan(ip, '1-1024', '-v  -sS')
    print(scanner.scaninfo())
    print(f"Status do IP: {scanner[ip].state()}")
    print(scanner[ip].all_protocols())
    print("Portas Abertas: ", scanner[ip]['tcp'].keys())