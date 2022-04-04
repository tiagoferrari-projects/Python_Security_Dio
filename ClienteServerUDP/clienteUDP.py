# importado biblioteca socket
import socket

# criado objeto de conexão
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('Cliente Socket Criado com Sucesso!')

host = 'localhost'
porta = 5433  # porta do cliente
mensagem = 'Olá Servidor, firmeza?!'

# tentar enviar e receber
try:
    print('Cliente: ' + mensagem)
    s.sendto(mensagem.encode(), (host, 5432))  # encodar: como se tivesse empacotando a msg e enviando com pacotes UDP
    # para o servidor

    dados, servidor = s.recvfrom(4096)
    dados = dados.decode()
    print('Cliente: ' + dados)
finally:
    print('Cliente: Fechado a conexa')
    s.close()
