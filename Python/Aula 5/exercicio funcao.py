i = 0
num = 0
maior = 0
menor = 0

def func_maior(n1,n2):
    if(n1>n2):
        numero_maior = n1
        return numero_maior
    else: 
        return n2
    
def func_menor(n1,n2,cont):
    if(cont==0):
        numero_menor = n1
        return numero_menor
    else:
        if(n1<n2):
            numero_menor = n1
            return numero_menor
        else:
            return n2
    

for i in range (0,5,1):
    num = int(input("Digite um número: "))
    maior = func_maior(num,maior)
    menor = func_menor(num,menor,i)
print(f"Maior: {maior}")
print(f"Menor: {menor}")