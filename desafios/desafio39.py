from datetime import date
nasc = int(input('Ano de nascimento: '))
atual = date.today().year
idade = atual - nasc
alistamento = nasc + 18
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
if idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para o alistamento.\nSeu alistamento será em {}.'.format(saldo, alistamento))
elif idade > 18:
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} anos.\nSeu alistamento foi em {}.'.format(saldo, alistamento))
else:
    print('Você tem que se alistar IMEDIATAMENTE!')