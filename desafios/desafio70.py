totalcompra = maisDeMil = contProduto = 0
nomeMaisBarato = ' '
nomeMaisCaro = ' '
print('--------LOJA SUPER BARATÃO--------')
while True:
    produto = str(input('Nome do produto: '))
    preço = float(input('Preço: R$'))
    contProduto += 1
    
    totalcompra += preço
    
    if preço >= 1000:
        maisDeMil += 1
        
    if contProduto == 1:
       maisCaro = maisBarato = preço
       nomeMaisCaro = nomeMaisBarato = produto
    else:
        if preço > maisCaro:
            maisCaro = preço 
            nomeMaisCaro = produto
        if preço < maisBarato:
            maisBarato = preço
            nomeMaisBarato = produto
    
    
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('--------FIM DO PROGRAMA--------')
print(f'O total da compra foi R${totalcompra:.2f}')
print(f'Temos {maisDeMil} produtos custando mais de R$1000,00')
print(f'O produto mais barato foi {nomeMaisBarato} que custa R${maisBarato:.2f}')
print(f'O produto mais caro foi {nomeMaisCaro} que custa R${maisCaro:.2f}')