print('==========LOJAS FERRAZ==========')
preco = float(input('Preço das compras: R$'))
print('FORMAS DE PAGAMENTO\n[ 1 ] à vista dinheiro/cheque\n[ 2 ] à vista cartão\n[ 3 ] 2x no cartão\n[ 4 ] 3x ou mais no cartão')
opção = int(input('Qual é a opção? '))
if opção == 1:
    desconto = preco - (preco * 0.1)
    print('Sua compra de {:.2f} vai custar {:.2f} no final.'.format(preco,desconto))
elif opção == 2:
    desconto = preco - (preco * 0.05)
    print('Sua compra de {:.2f} vai custar {:.2f} no final.'.format(preco,desconto))
elif opção == 3:
    parcelado = preco / 2
    print('Sua compra será parcelada em 2x de {:.2f} SEM JUROS'.format(parcelado))
    print('Sua compra vai custar {:.2f} no final.'.format(preco))
elif opção == 4:
    parcelas = int(input('Quantas parcelas? '))
    totjuros = preco + (preco * 0.2)
    parcelajuro = totjuros / parcelas
    print('Sua compra será parcelada em {}x de {:.2f} COM JUROS '.format(parcelas, parcelajuro,))
    print('Sua compra de {:.2f} vai custar {:.2f} no final.'.format(preco, totjuros))
else:
    print('ERRO! Digite um número válido, tente novamente')
    
    