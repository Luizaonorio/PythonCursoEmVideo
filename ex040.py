nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) /2

if media < 5:
    print('Aluno Reprovado! Nota final {}'.format(media))

elif media == 5 and media < 7:
    print('Aluno em recuperação! Nota final: {}'.format(media))

elif media >= 7:
    print('Aluno Aprovado! Nota final {}'.format(media))

else:
    print('Ouve um problema! Tente novamente.')