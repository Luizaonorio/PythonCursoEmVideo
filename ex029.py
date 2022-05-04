velocidade = float(input('Digite a velocidade: '))
if velocidade >80:
    print('Você foi multado! velocidade de {} excede o limite.'.format(velocidade))
    valor = (velocidade - 80) *7
    print('O valor da multa é de R${}'.format(valor))
else:
    print('Parabéns! Sem multas.')