
print('='*20)
print('   BANCO FERRAZ')
print('='*20)
while True:
    valor = float(input('Quanto quer sacar? R$'))
    
    cedulas_50 = valor // 50 #Quantas vezes 50 cabe dentro do valor
    resto = valor % 50 #Resto da divisão
    
    cedulas_10 = resto // 10 #Quantas vezes 10 cabe no restante da divisão anterior
    resto = resto % 10 #Reto da divisão
    
    cedulas_1 = resto
    break
print(f'Total de {cedulas_50:.0f} cédulas de R$50')
print(f'Total de {cedulas_10:.0f} cédulas de R$10')
print(f'Total de {cedulas_1:.0f} cédulas de R$1')
    
    