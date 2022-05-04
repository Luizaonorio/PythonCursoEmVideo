from datetime import date
ano = int(input('Digite seu ano de nascimento: '))
idade = 2021 - ano

if idade > 18:
    passou = idade - 18
    print('Passou do tempo do alistamento em {} anos'.format(passou))

elif idade < 18:
    falta = 18 - idade
    print('Ainda faltam {} anos.'.format(falta))

elif idade == 18:
    print('Está na hora de se alistar!')

else:
    print('Houve um problema. Tente novamente!')