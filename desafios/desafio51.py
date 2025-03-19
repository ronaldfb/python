print('''
=======================================   
        10 TERMOS DE UMA PA
=======================================
      ''')

p = int(input('Primeiro termo: '))
r = int(input('Razão: '))

for c in range(p, p+10):
    print(p, end=' → ')
    p += r
print('Acabou')