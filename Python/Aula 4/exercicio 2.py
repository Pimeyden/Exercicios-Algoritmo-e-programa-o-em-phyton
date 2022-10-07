vetor = [0.0]*50
i = 0

for i in range(0,50,1):
    vetor[i] = float(input("Informe um número para a posição " + str(i+1) + " do vetor: "))

    if(i%2 == 0):
        vetor[i] = vetor[i]*1.02
    else:
        vetor[i] = vetor[i]*1.05

print("Vetor Final")
for i in range(0,50,1):
    print(f"{vetor[i]}", end=' - ')
    