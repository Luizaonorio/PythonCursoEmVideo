from math import sin,cos, tan, hypot, radians

a = float(input('Digite o ângulo: '))
s = sin(radians(a))
c = cos(radians(a))
t = tan(radians(a))
print('No ângulo de {}, calculaos o seno {:.2f}, cosseno {:.2f} e a tangente {:.2f}'.format(a, s, c, t))