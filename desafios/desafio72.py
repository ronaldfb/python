numext = (
    'zero', 'um', 'dois', 'três', 'quatro', 
    'cinco', 'seis', 'sete', 'oito', 'nove', 
    'dez', 'onze', 'doze', 'treze', 'quatorze', 
    'quinze', 'dezesseis', 'dezessete', 'dezoito', 
    'dezenove', 'vinte'
)

while True:
    while True:
        try:
            num = int(input('Digite um número entre 0 e 20: '))
            if 0 <= num <= 20:
                break
            else:
                print('Valor fora do intervalo. Tente novamente.')
        except ValueError:
            print('Entrada inválida. Digite um número inteiro.')

    print(f'Você digitou o número {numext[num]}.')

    resp = input('Quer continuar? [S/N] ').strip().upper()
    while resp not in ('S', 'N'):
        resp = input('Resposta inválida. Quer continuar? [S/N] ').strip().upper()
    
    if resp == 'N':
        break

print('Fim do programa!')
    