salario = float(input("Digite o salário de um funcionario: "))

if(salario<=500):
    sal_final = salario + (salario*0.5)
elif((salario>500) and (salario<=1200)):
    sal_final = salario + (salario*0.12)
elif(salario>1200):
    sal_final = salario

if(salario<=600):
    print(f"Salário a receber: {sal_final+150} reais")
else:
    if(salario>600):
        print(f"Salario a receber {sal_final+100} reais")