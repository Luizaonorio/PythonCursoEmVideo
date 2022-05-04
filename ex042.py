r1 = float(input('Comprimento primeira reta: '))
r2 = float(input('Comprimento segunda reta: '))
r3 = float(input('Comprimento terceira reta: '))

if r1 < r3 + r2 and r2 < r3 + r1 and r3 < r2 + r1:
    print('As retas podem formar um triângulo!')

    if r1 == r2 == r3:
        print('Esse triângulo é equílatero.')

    if r1 == r2 != r3 or r2 == r3 != r1 or r3 == r1 != r2:
        print('Esse triângulo é isósceles.')

    if r1 != r2 != r3:
        print('Esse triângulo é escaleno')

else:
    print('As retas não podem formar um triângulo!')

