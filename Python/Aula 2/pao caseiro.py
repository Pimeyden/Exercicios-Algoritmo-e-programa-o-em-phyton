qtd_pao = int(input("Digite a quantidade vendida de caseirinhos: "))
qtd_broa = int(input("Digite a quantidade vendida de broinha: "))
total = 0.0
total = (qtd_pao * 0.10) + (qtd_broa * 1.60)

print(f"Valor vendido de Caseirinhos: {qtd_pao*0.10} reais")
print(f"Valor vendido de Broinhas: {qtd_broa*1.60} reais")
print(f"Valor total vendido: {total} reais")
print(f"Valor que deverá ser guardado na poupança: {total*0.1:,.2f} reais")