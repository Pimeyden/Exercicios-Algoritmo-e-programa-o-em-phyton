temp = 0.0
kilometragem = 0.0
velmedia = 0.0

velmedia = float(input("Digite a velocidade média que você fez a viagem: "))
temp = float(input("Digite o tempo gasto na viagem(em horas): "))
kilometragem = float(input("Digite quantos Km/l o seu carro faz: "))

print(f"Velocidade média: {velmedia} Km/h")
print(f"O tempo gasto foi de: {temp} horas")
distanciapercorrida = velmedia*temp
print(f"A distancia percorrida foi de: {distanciapercorrida} km")
quantidadelitros = distanciapercorrida/kilometragem
print(f"A quantidade de litros gasto foi de: {quantidadelitros:,.2f} litros")
