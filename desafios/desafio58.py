from random import randint
tentativas = 1
num = randint(0, 10)
res = int(input('Acabei de pensar em um número entre 0 e 10.\nSerá que você consegue adivinhar qual foi?\nQual é o seu palpite?'))
while res != num:
    if num > 4:
        print('Mais... Tente mais uma vez.')
        res = int(input('Qual é o seu palpite?'))
        tentativas += 1
    else:
        print('Menos... Tente mais uma vez.')
        res = int(input('Qual é o seu palpite?'))
        tentativas += 1
print('Acertou com {} tentativas. Parabéns!'.format(tentativas))
