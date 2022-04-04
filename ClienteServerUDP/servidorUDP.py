# importar biblioteca socket
import socket

# criado objeto de conexao
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('Socket criado com sucesso!!')

# viaraveis para armazenar e receber localhost e a porta
host = 'localhost'
porta = 5432

# fazer ligação cliente-servidor, através do host e porta
s.bind((host, porta))
mensagem = '\nServidor: Oláaaa cliente, e ai beleza?'

while 1:
    dados, end = s.recvfrom(4096)

    if dados:
        print('Servidor enviando mensagem ...')
        s.sendto(dados + (mensagem.encode()), end)
