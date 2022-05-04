n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

if n1 > n2:
    print('O \033[0;33mprimeiro valor\033[m {} é \033[0;34mmaior\033[m que o segundo {}.'.format(n1, n2))

elif n1 < n2:
    print('O \033[0;33msegundo valor\033[m {} é \033[0;34mmaior\033[m que o primeiro {}.'.format(n2, n1))

elif n1 == n2:
    print("\033[0;33mNão existe\033[m valor maior, os dois são \033[0;34miguais\033[m.")

else:
    print('Houve um problema, por favor, tente novamente! ')