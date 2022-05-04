real = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar1 = real / 3.27
dolar2 = real / 6.18
print('Com R${} você pode comprar U${:.2f} em 2017 e U${:.2f} em 2022'.format(real, dolar1, dolar2))