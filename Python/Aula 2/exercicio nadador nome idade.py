nome = input("Digite o nome do nadador: ")
idade = int(input("Digite a idade do nadador: "))

if((idade>=5) and (idade<=7)):
    print(f"{nome} você tem {idade} ano(s)e está na categoria Infantil A")
elif((idade>=8) and (idade<=11)):
    print(f"{nome} você tem {idade} ano(s) e stá na categoria Infantil B")
elif((idade>=12) and (idade<=13)):
    print(f"{nome} você tem {idade} ano(s) e está na categoria Juvenil A")
elif((idade>=14) and (idade<=17)):
    print(f"{nome} você tem {idade} ano(s) e está na categoria Juvenil B")
elif(idade>=18):
    print(f"{nome} você tem {idade} ano(s) e está na categoria Adulto! ")
else:
    print(f"{nome}você tem {idade} ano(s) e não possui uma categoria válida.")