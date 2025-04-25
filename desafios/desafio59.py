from time import sleep
v1 = int(input('Primeiro valor: '))
v2 = int(input('Segundo valor: '))
sair = False
while not sair:
    print('[ 1 ] somar\n[ 2 ] multiplicar\n[ 3 ] maior\n[ 4 ] novos números\n[ 5 ] sair do programa')
    opcao = int(input('>>>>>>> Qual é sua opção? '))
    if opcao == 5:
        sair = True
    elif opcao == 1:
        soma = v1 + v2
        print('A soma entre {} e {} é {}'.format(v1,v2,soma))
    elif opcao == 2:
        mult = v1 * v2
        print('O resultado de {} x {} é {}'.format(v1,v2,mult))
    elif opcao == 3:
        if v1 == v2:
            print('Os dois valores são iguais!')
        elif v1 > v2:
            print('Entre {} e {} o maior valor é {}'.format(v1,v2,v1))
        else:
            print('Entre {} e {} o maior valor é {}'.format(v1,v2,v2))
    elif opcao == 4:
        print('Informe os números novamente:')
        v1 = int(input('Primeiro valor: '))
        v2 = int(input('Segundo valor: '))
    else:
        print('Opção inválida! tente novamente.')
    print('-='*16)
    sleep(1.6)
print('Fim da execução do programa.')
