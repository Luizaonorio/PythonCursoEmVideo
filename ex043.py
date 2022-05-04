altura = float(input('Digite sua altura: '))
peso = float(input('Digite o seu peso: '))
IMC = peso / (altura **2)

if IMC < 18.5:
    print('IMC = {:.2f}, considerado abaixo do peso!'.format(IMC))

elif IMC <= 25:
    print('IMC {:.2f}, considerado peso ideal!'.format(IMC))

elif IMC <= 30:
    print('IMC {:.2f}, considerado sobrepeso!'.format(IMC))

elif IMC <= 40:
    print('IMC {:.2f}, considerado obesidade.'.format(IMC))

elif IMC > 40:
    print('IMC {}, considerado obesidade morbída.')

else:
    print('Ocorreu um problema! Tente novamente. ')
