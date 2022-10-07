salminimo = float(input ("Digite o salário mínimo: "))
horastrab = int (input("Digite a quantidade de horas trabalhadas: "))
dependentesfunc = int (input("Digite o número de dependentes do funciónario: "))
horasextra = int (input("Digite a quantidade de horas extras: "))

valorhora = salminimo*0.2
salmes = horastrab*valorhora
dependentevalor = dependentesfunc*32.00
valorhoraextra= valorhora + (valorhora*0.5)
totalhoraextra = valorhoraextra * horasextra
salbruto = salmes + dependentevalor + totalhoraextra

if (salbruto < 200.00):
    irrpf = 0
    salliquido = salbruto + irrpf
elif (salbruto>= 200.00) and (salbruto <=500.00):
    irrpf = salbruto*0.1
    salliquido = salbruto - irrpf
elif(salbruto>500.00):
    irrpf = salbruto * 0.2
    salliquido = salbruto - irrpf

if (salliquido<= 350.00):
    gratif = 100.00
elif(salliquido> 350.00):
    gratif = 50.00

salfinal = salliquido + gratif

print(f"O salário final a receber é {salfinal:.2f} reais")