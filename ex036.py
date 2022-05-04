casa = float(input('Valor da casa: '))
salario = float(input('Salário: '))
anos = int(input('Anos: '))
por = (salario * 1.30) - salario
mes = casa / (anos * 12)
if mes > por:
    print('\033[1:31mEmprestimo negado! saldo insuficiente. \033[m \nValor mensal: R${:.2f} \nValor máximo: R${:.2f}'.format(mes, por))
elif mes < por:
    print('\033[1:34mEmprestimo aceito! \033[m \nO valor de R${:.2f} mensal é dentro do seu limite de R${:.2f}. '.format(mes, por))
else:
    print('Estamos com um problema. Por favor retorne mais tarde!')