i = 0
vetor = [0]*10

for i in range(0,10,1):
    vetor[i] = int(input("Informe um número que vai ser colocado na posição "+ str(i+1) + " do vetor: "))

for i in range(9,-1,-1):
    print(vetor[i], end =' - ')