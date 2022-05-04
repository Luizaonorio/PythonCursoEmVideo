km = float(input('Distância em km: '))
if km < 200:
    print('O valor a ser pago é: {}'.format(km * 0.50))

else:
    print('O valor a ser pago é de: {}'.format(km * 0.45))