salario = float(input('Qual  o slãrio do funcionário? R$'))
novo_salario = salario + salario * 15 / 100
print('Um funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format(salario, novo_salario))