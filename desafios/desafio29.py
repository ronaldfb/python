vel = float(input('Qual é a velocidade atual do carro? '))
if vel <= 80:
    print('Tenha um bom dia! Dirija com segurança!')
else:
    multa = (vel - 80) * 7
    print('Multado! Você excedeu o limite permitido que é de 80Km/h\nVocê deve pagar uma multa de R${:.2f}'.format(multa))