from random import shuffle

n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
n = [n1, n2, n3, n4]
p = shuffle(n)
print('A sequência escolhida foi: ')
print(n)