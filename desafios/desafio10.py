real = float(input('Quantos reais você tem? R$'))
taxa_cambio = 5.77
valor_dolares = real / taxa_cambio
print('Com R${:.2f} você pode comprar US${:.2f}'.format(real,valor_dolares))