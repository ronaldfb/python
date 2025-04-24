from time import sleep
v1 = int(input('Primeiro valor: '))
v2 = int(input('Segundo valor: '))
sair = False
while not sair:
    sleep(1.2)
    print('[ 1 ] somar\n[ 2 ] multiplicar\n[ 3 ] maior\n[ 4 ] novos números\n[ 5 ] sair do programa')
    opcao = int(input('>>>>>>> Qual é sua opção? '))
    if opcao == 5:
        sair = True
    elif opcao == 1:
        soma = v1 + v2
        sleep(0.5)
        print('A soma entre {} e {} é {}'.format(v1,v2,soma))
    elif opcao == 2:
        mult = v1 * v2
        sleep(0.5)
        print('O resultado de {} x {} é {}'.format(v1,v2,mult))
    elif opcao == 3:
        sleep(0.5)
        if v1 == v2:
            print('Os dois valores são iguais!')
        elif v1 > v2:
            print('O valor {} é maior que {}'.format(v1,v2))
        else:
            print('O valor {} é maior que {}'.format(v2,v1))
    elif opcao == 4:
        sleep(0.5)
        v1 = int(input('Primeiro valor: '))
        v2 = int(input('Segundo valor: '))
sleep(1)
print('Fim da execução do programa.')
