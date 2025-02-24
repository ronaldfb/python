from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
jogador = int(input('Suas opções:\n[ 0 ] PEDRA\n[ 1 ] PAPEL\n[ 2 ] TESOURA\nQual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!')
print('-=-'*10)
print('O computador jogou {}'.format(itens[computador]))
print('O jogador jogou {}'.format(itens[jogador]))
print('-=-'*10)
if computador == 0:
    if jogador == 0:
        print('Empate, ninguém venceu')
    elif jogador == 1:
        print('Jogador venceu')
    elif jogador == 2:
        print('Computador venceu')
    else:
        print('Jogada inválida!')
elif computador == 1:
    if jogador == 0:
        print('Computador venceu')
    elif jogador == 1:
        print('Empate, ninguém venceu')
    elif jogador == 2:
        print('Jogador venceu')
    else:
        print('Jogada inválida!')
elif computador == 2:
    if jogador == 0:
        print('Jogador venceu')
    elif jogador == 1:
        print('Computador venceu')
    elif jogador == 2:
        print('Empate, ninguém venceu')
    else:
        print('Jogada inválida!')

