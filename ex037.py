num = int(input('Digite um número qualquer inteiro: '))
c = int(input('\033[0;34mBase de conversão: '
              '\n1\033[m para \033[0;33mbinário\033[m '
              '\n\033[0;34m2\033[m para \033[0;33moctal\033[m '
              '\n\033[0;34m3\033[m para \033[0;33mhexadecimal\033[m '
              '\nDigite a conversão de sua escolha: '))

if c == 1:
    print('O número {} em binário é {}'.format(num, bin(num)[2:]))

elif c == 2:
    print('O número {} em octal é {}'.format(num, oct(num)[2:]))

elif c == 3:
    print('O número {} em octal é {}'.format(num, hex(num)[2:]))

else:
    print('Desculpe, tivemos um problema. Volte mais tarde!')