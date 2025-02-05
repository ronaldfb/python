km = float(input('Qual é a distancia da sua viagem? '))
# if km <= 200:
#     price = km * 0.50
# else:
#     price = km * 0.45
# print('Você está prestes a começar uma viagem de {:.1f}Km.\nE o preço da sua passagem será: R${:.2f}'.format(km,price))
price = km * 0.50 if km <= 200 else km * 0.45
print('Você está prestes a começar uma viagem de {:.1f}Km.\nE o preço da sua passagem será: R${:.2f}'.format(km,price))
    