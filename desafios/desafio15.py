dias_alugados = int(input('Quantos dias alugado? '))
km_rodados = float(input('Quantos Km rodados? '))
total = (dias_alugados * 60) + (km_rodados * 0.15)
print('O total a pagar é de R${:.2f}'.format(total))