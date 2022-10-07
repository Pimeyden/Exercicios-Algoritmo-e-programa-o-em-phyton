'''
programa que recebe uma medida em pés e calcule em polegada, jardas, e milhas
1 pé = 12 polegada
1 jarda = 3 pés
1 milha = 1760
'''

pes = 0.0

pes = float(input("Digite a medida em pés: "))

print(f"medida em pés: {pes}")
print(f"medida em polegada: {pes*12}")
print(f"medida em jardas: {(pes/3):,.2f}")
print(f"medida em milhas: {((pes/3)/1760):,.5f}")
