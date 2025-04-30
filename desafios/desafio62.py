print('Gerador de PA')
print('=-='*8)
pt = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
termo = pt
c = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while c <= total:
        print('{} → '.format(termo), end='')
        termo = termo + r
        c += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))