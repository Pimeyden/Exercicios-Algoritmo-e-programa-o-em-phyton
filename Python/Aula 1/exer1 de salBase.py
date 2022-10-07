'''
algortimo que recebe um salario base e mostre o salario a receber 
(deve pagar imposto de 10% e recebe bonificação de 50.00)
'''
sal = 0.0

sal = float(input("Digite o salário base: "))
print(f"O salário a receber é: {(sal-(sal*0.1))+50}")
