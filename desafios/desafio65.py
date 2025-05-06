resp = 'S'
cont = soma = maior = menor = 0
while resp in 'Ss':
    n = int(input('Digite um número: '))
    resp = str(input('Quer continuar? [S/N] ')).upper()
    cont += 1
    soma += n
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
media = soma/cont
print('Você digitou {} números e a média foi {}'.format(cont, media))
print('O maior valor foi {} e o menor valor foi {}'.format(maior, menor))
    