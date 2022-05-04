from random import randint

computador = randint(1, 5)
jogador = int(input('Digite um número entre 1 e 5: '))

if jogador == computador:
    print('Parabéns! Você escolhemos {}')
else:
    print('Se lascou, você escolheu {} e eu {}. I am the winner!!!'.format(jogador, computador))