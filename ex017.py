from math import hypot
ca = float(input('Digite o comprimento do cateto adjacente: '))
co = float(input('Digite o comprimento do cateto oposto: '))
h = hypot(co, ca)
print('A hipotenusa é {}'. format(h))