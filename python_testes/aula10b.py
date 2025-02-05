nome = str(input("Digite o nome do aluno(a): "))
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda note: "))
m = (n1 + n2) / 2
if m >= 6.0:
    print("Parabéns {} sua média foi de {:.1f}, você passou!".format(nome,m))
else: 
    print("{} sua média foi {:.1f} e você não atingiu a média para passar, Recuperação!".format(nome,m))