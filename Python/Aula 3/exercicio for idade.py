pessoa = int (input("Digite a quantidade de pessoas: "))
somaidade = 0
maior = 0
menor = 0
for i in range(0,pessoa,1):
    idade = int (input(f"Digite a idade da pessoa {i+1}: "))
    #somaidade = somaidade + idade
    somaidade += idade
    if(i==1):
        maior = idade
        menor = idade
    else:
        if(idade>maior):
            maior = idade
        elif(idade<menor):
            menor = idade

print(f"Média das idade digitadas: {somaidade/pessoa:.2f}")
print(f"Maior: {maior}")
print(f"Menor: {menor}")
