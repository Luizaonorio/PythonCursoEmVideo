valor = float(input('Digite o valor bruto do produto: '))
pagamento = int(input('''\033[0;34mDigite a forma de pagamento correspondente:\033[m
\033[1;32m1\033[m para á vista \033[1;33mdinheiro/cheque\033[m
\033[1;32m2\033[m para á vista no \033[1;33mcartão\033[m
\033[1;32m3\033[m para em até \033[1;33m2x no cartão\033[m
\033[1;32m4\033[m para em \033[1;33m3x ou mais no cartão\033[m
forma:'''))

if pagamento == 1:
    din = valor * 1.10
    print('Valor com desconto é {:.2f}'.format(din))

elif pagamento == 2:
    car1 = valor * 1.05
    print('Valor com desconto é {:.2f}'.format(car1))

elif pagamento == 3:
    print('Valor da compra: R${:.2f}'.format(valor))

elif pagamento == 4:
    car2 = (valor * 0.20) + valor
    print('Valor do produto com juros de 20%: R${:.2f}'.format(car2))