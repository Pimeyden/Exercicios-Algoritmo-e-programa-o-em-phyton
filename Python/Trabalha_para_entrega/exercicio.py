#bibliotecas
import random
import os

#variáveis
mat = [[0]*3,[0]*3,[0]*3,[0]*3,[0]*3,[0]*3,[0]*3,[0]*3,[0]*3,[0]*3,[0]*3,[0]*3,[0]*3,[0]*3,[0]*3,[0]*3,[0]*3,[0]*3,[0]*3,[0]*3,[0]*3,[0]*3,[0]*3,[0]*3,[0]*3,[0]*3,[0]*3,[0]*3,[0]*3,[0]*3,[0]*3,[0]*3,[0]*3,[0]*3,[0]*3,[0]*3,[0]*3,[0]*3,[0]*3,[0]*3]
nota = [[0.0]*4,[0.0]*4,[0.0]*4,[0.0]*4,[0.0]*4,[0.0]*4,[0.0]*4,[0.0]*4,[0.0]*4,[0.0]*4,[0.0]*4,[0.0]*4,[0.0]*4,[0.0]*4,[0.0]*4,[0.0]*4,[0.0]*4,[0.0]*4,[0.0]*4,[0.0]*4,[0.0]*4,[0.0]*4,[0.0]*4,[0.0]*4,[0.0]*4,[0.0]*4,[0.0]*4,[0.0]*4,[0.0]*4,[0.0]*4,[0.0]*4,[0.0]*4,[0.0]*4,[0.0]*4,[0.0]*4,[0.0]*4,[0.0]*4,[0.0]*4,[0.0]*4,[0.0]*4]
opc = ""
esc = 0
soma = 0.0
media = 0.0
opc2 = ""
q = 1 #mudar para a quantidade de alunos até 40

#algoritmo
for j in range(q):    
    mat[j][1] = int(input(f"Informe o RA do aluno {j+1}: "))
    mat[j][2] = int(input(f"Informe o CPF do aluno {j+1}: "))
    mat[j][0] = int(input(f"Informe o código do aluno {j+1}: "))
'''
    print(f"Informe o RA do aluno {j+1}: ")
    mat[j][1] = random.randint(1000000,9999999)
    print(f"Informe o CPF do aluno {j+1}: ")
    mat[j][2] = random.randint(10000000000,99999999999)
    print(f"Informe o código do aluno {j+1}: ")
    mat[j][0] = random.randint(1,999)
'''

    #os.system("clear||cls")

for j in range(q):
    for k in range(4):
        nota[j][k] = float(input(f"Informe a nota {k+1} do aluno {j+1}: "))
    '''
        print(f"Informe a nota {k+1} do aluno {j+1}: ")
        nota[j][k] = random.uniform(0.0,10.0)
        os.system("clear||cls")
    '''

for j in range(q):
    print(f"Aluno {j+1}")
    print(f"Código: {mat[j][0]}")
    print(f"RA: {mat[j][1]}")
    print(f"CPF: {mat[j][2]}")
    for k in range(4):
        print (f"Nota {k+1}: {nota[j][k]:.2f}")
    print("\n")

while opc2 != 'N':
    op = ""
    esc = 0
    print("Escolha uma das opções à seguir:")
    print("1 - RA do aluno\n2 - CPF do aluno\n3 - Código do aluno")
    opc = input("Insira a opção desejada: ")

    match opc:
        case '1':
            while  op!= '2':
                soma = 0.0
                media = 0.0
                j = 0
                os.system("clear||cls")
                esc = int(input("Insira o RA do aluno: "))
                for j in range(q):
                    if esc==mat[j][1]:
                        print(f"RA do aluno: {mat[j][1]}")
                        for k in range(4):
                            print(f"Nota {k+1}: {nota[j][k]:.2f}")
                            soma += nota[j][k]
                        media = soma/4.0
                        print(f"Média = {media:.2f}")
                        p = mat[j][1];
                        op = '2';
                if esc != mat[j][1] and esc != p:
                    esc = 0
                    op = input("O RA informado não foi encontrado!\nInsira 1 para tentar novamente ou 2 para escolher outra opção: ")
        case '2':
            while op!= '2':
                soma = 0.0
                media = 0.0
                j = 0
                os.system("clear||cls")
                esc = int(input("Insira o CPF do aluno: "))
                for j in range(q):
                    if esc==mat[j][2]:
                        print(f"CPF do aluno: {mat[j][2]}")
                        for k in range(4):
                            print(f"Nota {k+1}: {nota[j][k]:.2f}")
                            soma += nota[j][k]
                        media = soma/4.0
                        print(f"Média = {media:.2f}")
                        p = mat[j][2];
                        op = '2';
                if esc != mat[j][2] and esc != p:
                    esc = 0
                    op = input("O CPF informado não foi encontrado!\nInsira 1 para tentar novamente ou 2 para escolher outra opção: ")
        case '3':
            while op!= '2':
                soma = 0.0
                media = 0.0
                j = 0
                os.system("clear||cls")
                esc = int(input("Insira o código do aluno: "))
                for j in range(q):
                    #print (mat[j][0])
                    #print (esc)
                    #print (esc==mat[j][0])
                    if esc==mat[j][0]:
                        print(f"Código do aluno: {mat[j][0]}")
                        for k in range(4):
                            print(f"Nota {k+1}: {nota[j][k]:.2f}")
                            soma += nota[j][k]
                        media = soma/4.0
                        print(f"Média = {media:.2f}")
                        p = mat[j][0];
                        op = '2';
                if esc != mat[j][0] and esc != p:
                    esc = 0
                    op = input("O código informado não foi encontrado!\nInsira 1 para tentar novamente ou 2 para escolher outra opção: ")
        case _:
            os.system("clear||cls")
            print("Opção inválida!")
    opc2 = input("Deseja continuar a consulta (S-sim/N-não)?")
    opc2 = opc2.upper()
        