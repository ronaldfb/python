listagem = ('Borracha', 2,
            'Lápis', 1.24,
            'Caderno', 7.80,
            'Caneta', 1.50,
            'Mochila', 59.99,
            'Estojo', 11.45,
            'Livro', 30)
print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')
    