from random import randint
números = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print('Sorteei os valores: ', end='')
for n in números:
    print(f'{n} ', end='')
# maior = números[0]
# menor = números[0]
# for n in números:
#     if n > maior:
#         maior = n
#     if n < menor:
#         menor = n
# print(f'O maior número foi {maior} e o menor número foi {menor}')
print(f'\nO maior valor sorteado foi {max(números)}')
print(f'O menor valor sorteado foi {min(números)}')
    
    
   