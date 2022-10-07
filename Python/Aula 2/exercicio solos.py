ponto_agua = float (input("Digite a quantidade de pontos de água presentes na amostra do solo: "))


if(ponto_agua <=10):
    print("O solo em análise é Rochoso")
elif((ponto_agua >10) and (ponto_agua<=40)):
    print("O solo em análise é Firme")
elif((ponto_agua > 40) and (ponto_agua<=80)):
    print("O solo em análise é Pantanosa")
else:
    print("Quantidade inválida")

'''
if(ponto_agua <=10):
    print("O solo em análise é Rochoso")
else:
    if((ponto_agua >10) and (ponto_agua<=40)):
        print("O solo em análise é firme")
    else:
        if((ponto_agua > 40) and (ponto_agua<=80)):
            print("O solo em análise é Pantanosa")
        else:
            print("Quantidade inválida")
'''
