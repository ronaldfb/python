numext = ('zero', 'um', 'dois', 'três', 'quatro', 
          'cinco', 'seis', 'sete', 'oito', 'nove', 
          'dez', 'onze', 'doze', 'treze', 'quatorze', 
          'quinze', 'dezesseis', 'dezessete', 'dezoito', 
          'dezenove', 'vinte')
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    while num <0 or num > 20:
        print('Tente novamente. ', end='')
        num = int(input('Digite um número entre 0 e 20: '))
    if num >= 0 and num <= 20:
        print(f'Você digitou o número {numext[num]}')     
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('Fim do programa! ')
    