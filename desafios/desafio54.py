from datetime import date
maiorDeIdade = 0
menorDeIdade = 0
atual = date.today().year
for c in range(1, 8):
    nasc = int(input('Em que ano a {} pessoa nasceu? '.format(c)))
    if nasc <= atual - 18:
        maiorDeIdade += 1
    else:
        menorDeIdade += 1
print('Ao todo tivemos {} pessoas maiores de idade\nE também tivemos {} pessoas menores de idade'.format(maiorDeIdade, menorDeIdade))
