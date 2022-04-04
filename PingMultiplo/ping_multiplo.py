from os import system # importando biblioteca os
from time import sleep # importando biblioteca time


with open('hosts.txt') as file: # com abertura do arquivo
    dump = file.read()          # criado variavel dump, ler o arquivo dentro do dump
    dump = dump.splitlines()    # organiza os ips em linhas separadas

    for ip in dump:
        print('Verificando IP: ' + ip)
        print('-' * 60)
        system('ping -c 2 {}'.format(ip)) # executa o comando ping enviando 2 pacotes com saida formatada
        print('-' * 60)
        sleep(5) # espera 5s o tempo de execuçao de um comando para o outro
