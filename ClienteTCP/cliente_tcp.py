import socket
import sys  # fornece o acesso a algumas variáveis e funções que tem forte interação com o interpretador


def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as e:
        print('A conexão falhou!!!')
        print('Erro: {}'.format(e))
        sys.exit()

    print('Socket criado com sucesso!!!')

    host_alvo = input('Digite o Host ou Ip a ser conectado: ')
    porta_alvo = input('Digite a porta a ser conectada: ')

    try:
        s.connect((host_alvo, int(porta_alvo)))
        print('Cliente TCP conectado com Sucesso no Host: {} e na Porta: {}'.format(host_alvo, porta_alvo))
        s.shutdown(3)
    except socket.error as e:
        print('Não foi possível conectar no Host: {} - Porta: {}'.format(host_alvo, porta_alvo))
        print('Erro: {}'.format(e))
        sys.exit()


if __name__ == '__main__':
    main()
