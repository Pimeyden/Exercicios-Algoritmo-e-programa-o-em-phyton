canal = 1
qtd9 = 0.0
qtd12 = 0.0
qtd23 = 0.0
qtd40 = 0.0
qtdOutro = 0.0
totalcanal = 0.0
while canal != 0:
    canal = int (input("Digite o canal (9, 12, 23 ou 40: (0 para fechar): "))
    totalcanal += 1    
    if(canal== 9): 
        qtd9 += 1
    else:
        if(canal==12):
            qtd12 += 1
        else:
            if(canal==23):
                qtd23 += 1
            else:
                if(canal==40):
                    qtd40 += 1
                else:
                    if(canal!=0):
                        qtdOutro += 1

totalcanal = totalcanal - 1 

print(f"Porcentagem do canal 9: {(qtd9/totalcanal)*100}%")
print(f"Porcentagem do canal 12: {(qtd12/totalcanal)*100}%")
print(f"Porcentagem do canal 23: {(qtd23/totalcanal)*100}%")
print(f"Porcentagem do canal 40: {(qtd40/totalcanal)*100}%")
print(f"Porcentagem de outros canais: {(qtdOutro/totalcanal)*100}%")
