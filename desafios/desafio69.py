continuar = 'S'
maiorDeIdade = 0
contHomem = 0
contMulher = 0
while continuar == 'S':
    print('--'*25)
    print('  CADASTRE UMA PESSOA')
    print('--'*25)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    print('--'*25)
    continuar = str(input('quer continuar? [S/N] ')).strip().upper()[0]
    if idade > 18:
        maiorDeIdade += 1
    if sexo == 'M':
        contHomem += 1
    if sexo == 'F' and idade<20:
        contMulher += 1       
print(f'Total de pessoas com mais de 18 anos: {maiorDeIdade}')
print(f'Ao todo temos {contHomem} homens cadastrados')
print(f'E temos {contMulher} mulheres com menos de 20 anos')
    