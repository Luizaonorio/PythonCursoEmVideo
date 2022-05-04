d = int(input('Dias alugados: '))
km = float(input('Km rodado: '))
pag = (d * 60) + (km * 0.15)
print('O total a pagar é: {}'.format(pag))