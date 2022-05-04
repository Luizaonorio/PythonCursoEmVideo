from datetime import date
nascimento = int(input('Digite seu ano de nascimento: '))
ano = date.today().year
idade = ano - nascimento

if idade <= 9:
    print('Com {}, sua categoria é mirim'.format(idade))

elif  idade <= 14:
    print('Com {}, sua categoria é infantil'.format(idade))

elif idade <= 19:
    print('Com {}, sua categoria é junior.'.format(idade))

elif idade <= 20:
    print('Com {}, sua categoria é sênior.'.format(idade))

elif idade > 20:
    print('Com {}, sua categoria é master.'.format(idade))

else:
    print('Ocorreu um erro! Por favor, tente novamente.')