lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
#Tuplas são imutáveis 
#lanche[1] = 'Refrigerante' <--- não tem como fazer isso!
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi bastante!')