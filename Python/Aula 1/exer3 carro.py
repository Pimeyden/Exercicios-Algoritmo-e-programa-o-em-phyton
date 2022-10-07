'''
recebe preço fabrica, percentual de distribuidor e de imposto, mostre tudo e preço final
'''

precofabrica,porcentlucro,porcentimpost = 0.0,0.0,0.0

precofabrica = float(input("Digite o preço de fábrica do carro: "))
porcentlucro = float(input("Digite o percentual do lucro do distribuidor: "))
porcentimpost = float(input("Digite o percentual de imposto: "))

print(f"O valor correspondente ao lucro do distruibuidor é: {precofabrica*(porcentlucro/100)}")
print(f"O valor do imposto é:  {precofabrica*(porcentimpost/100)}")
print(f"O preço final do carro é: {(precofabrica*porcentlucro/100)+(precofabrica*porcentimpost/100)+ precofabrica}")
