#Exercicio 3

matriz = [[0]*5, [0]*5, [0]*5, [0]*5, [0]*5]
i,j = 0,0

for i in range(0,5,1):
    for j in range(0,5,1):
        matriz[i][j] = int(input("Informe um número para posição(" + str(i+1) + "," + str(j+1) + ") da matriz: "))

for i in range(0,5,1):
    for j in range(0,5,1):
        if i == j:
            print(f"{matriz[i][j]}")
        else:
            print(end=' ')
    print("  ")
    