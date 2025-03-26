totidade = 0
totmulher = 0
homemvelho = 0
nomemaisvelho = ''
for p in range(1, 5):
    print('----- {}ª Pessoa -----'.format(p))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    if p == 1:
        totidade = idade
    else:
        totidade += idade
    sexo = str(input('[M/F]: ')).upper()
    if sexo == 'F'and idade < 20:
     totmulher += 1
    
    if sexo == 'M' and idade > homemvelho:
        homemvelho = idade
        nomemaisvelho = nome
     
mediaidade = totidade/4
print('-------------------------------------------------------------')
print('A média de idade do grupo é de {} anos.'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}.'.format(homemvelho, nomemaisvelho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(totmulher))
    
    
    