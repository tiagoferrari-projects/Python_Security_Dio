import os # Importa o módulo ou biclioteca os ( integra os programas e recursos do S.O

print('#' * 60) ## Imprimindo # 60 vezes

ip_ou_host = input('Digite o IP ou HOST a ser verificado: ')
# criado uma variável que vai receber do usuário um ip
print('-' * 60) ## Imprimindo # 60 vezes
os.system('ping -c 3 {}'.format(ip_ou_host)) ## chamando system da biblioteca os - comando ping
# -c númerodepacotes que serão 3 {}
print('-' * 60) ## Imprimindo # 60 vezes
