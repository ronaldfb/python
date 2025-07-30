tabela = ('Flamengo', 'Cruzeiro', 'Palmeiras', 'Bahia', 'Bragantino', 'Botafogo,',
          'Mirassol', 'São Paulo', 'Ceará', 'Internacional', 'Corinthians',
          'Fluminense', 'Atlético-MG', 'Grêmio', 'Vitória', 'Vasco da Gama',
          'Santos', 'Fortaleza', 'Juventude', 'Sport Recife')
print('=-'*20)
print(f'Tabela Brasileirão: {tabela}')
print('=-'*20)
print(f'Os 5 primeiros são: {tabela[0:5]}')
print('=-'*20)
print(f'Os 4 ultimos são: {tabela[-4:]}')
print('=-'*20)
print(f'Times em ordem alfabética {sorted(tabela)}')
print(f'O Santos esta na {tabela.index('Santos')+1}ª posição :(')

