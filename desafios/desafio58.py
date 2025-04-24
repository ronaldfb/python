"""
from random import randint
tentativas = 1
num = randint(0, 10)
res = int(input('Acabei de pensar em um número entre 0 e 10.\nSerá que você consegue adivinhar qual foi?\nQual é o seu palpite? '))
while res != num:
    if num > res:
        print('Mais... Tente mais uma vez.')
        res = int(input('Qual é o seu palpite? '))
        tentativas += 1
    else:
        print('Menos... Tente mais uma vez.')
        res = int(input('Qual é o seu palpite? '))
        tentativas += 1
print('Acertou com {} tentativas. Parabéns!'.format(tentativas))
"""
from random import randint
computador = randint(0,10)
print('Acabei de pensar em um número entre 0 e 10.\nSerá que você consegue adivinhar qual foi?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... tente mais uma vez.')
        elif jogador > computador:
            print('Menos... tente mais uma vez')
print('Acertou com {} tentativas. Parabéns!'.format(palpites))
