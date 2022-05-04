frase = str(input('Digite uma frase: ')).strip().upper()
print('Vezes que aparecem a: {}'.format(frase.count('A')))
print('Primeira vez aparecendo: {}'.format(frase.find('A')+1))
print('Ultimma vez aparecendo é: {}'.format(frase.rfind('A')+1))