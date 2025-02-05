from random import randint
from time import sleep
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
num = randint(0, 5)
res = int(input('Em que número eu pensei?'))
print('PROCESSANDO...')
sleep(2)
if num == res:
    print('PARABÉNS! Você adivinhou o número e ganhou.')
else:
    print('GANHEI! O número que eu pensei foi {} e não no {}. '.format(num,res))
