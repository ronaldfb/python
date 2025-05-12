# cont = 0
# while True:
#     num = int(input('Quer ver a tabuada de qual valor? '))
#     if num < 0:
#         break  
#     print('-'*50)
#     while cont <=10:
#         mult = num*cont
#         print(f'{num} x {cont} = {mult}' )
#         cont += 1
#     cont = 0
#     print('-'*50)
# print('Programa tabuada encerrado!')  
while True:
    num = int(input('Quer ver a tabuada de qual valor? '))
    if num < 0:
        break
    print('='*40)
    for cont in range(1,11):
        print(f'{num} x {cont} = {num*cont}' )
        cont += 1
    print('='*40)
print('Programa tabuada encerrado!')
    