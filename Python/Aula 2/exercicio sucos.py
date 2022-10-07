'''
algoritmo que revende sucos, receba a quantidade de latas, garrafa de 600
e garrafa de 2 litros, exiba o total de litros revendido
'''

total = 0.0
lata = int(input("Digite a Quantidade de latas de 350ml: "))
total = total + (lata*350)
garrafa600 = int(input("Digite a Quantidade de garrafas de 600ml: "))
total = total + (garrafa600*600)
garrafa2lts = int(input("Digite a Quantidade de garrafa de 2lts: "))
total = total + (garrafa2lts*2000)

print(f"A quantidade em litros digitado foi de {total/1000} litros")