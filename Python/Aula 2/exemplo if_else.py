
nome = input("Informe o nome o aluno: ")
n1 = float(input("Digite a nota 1: "))
n2 = float(input("Digite a nota 2: "))
media = 0.0
situacao = ""

media=(n1+n2)/2

if(media >= 6):
    situacao = "aprovado"
else:
    if(media >=4) and (media <6):
        situacao = "recuperação"
    else:
        situacao = "reprovado"

print(f"{nome} sua média é: {media:,.1f} e você está {situacao}!!")