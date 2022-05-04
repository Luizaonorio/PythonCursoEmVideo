nome = str(input('Digite seu nome: ')).strip()
n = nome.split()
print('Primeiro: {}'.format(n[0]))
print('Segundo: {}'.format(n[len(n)-1]))