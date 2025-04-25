print('Gerador de PA')
print('=-='*8)
pt = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
termo = pt
c = 1
while c <= 10:
    print('{} → '.format(termo), end='')
    termo = termo + r
    c += 1
print('FIM')







# print('Gerador de PA')
# print('=-='*8)
# pt = int(input('Primeiro termo: '))
# r = int(input('Razão da PA: '))
# c = 1
# while c <= 10:
#     print('{}'.format(pt), end=' → ')
#     pt += r
#     c += 1
# print('Fim')