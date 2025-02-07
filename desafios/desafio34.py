sal = float(input('Qual é o salário do funcionário? R$'))
if sal <= 1250:
    aumento = sal * 0.15 + sal
else:
    aumento = sal * 0.10 + sal
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(sal,aumento))

