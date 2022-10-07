tipo_carro = input ("Informe o tipo do carro (G)gasolina ou (A)alcool: ")
tipo_carro= tipo_carro.upper()
if(tipo_carro == "G"):
    tipo_carro = "Gasolina"
elif(tipo_carro == "A"):
    tipo_carro = "Alcool" 
else:
    print("Tipo de carro inválido")
    exit()
capacidade_tanque = int(input("Informe a capacidade de litros: "))

print(f"Então seu carro é a {tipo_carro} e a capacidade dele é {capacidade_tanque} litros")
valor_litro = float(input(f"Digite o valor do litro atual da {tipo_carro}: "))

print(f"O preço para encher o tanque é: {capacidade_tanque*valor_litro} reais")

