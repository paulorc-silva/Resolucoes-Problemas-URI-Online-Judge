lista = []

for num in range(0, 10, 1):
    lista.append(int(input("Digite um número: ")))

maior = lista[0]
    
for i in range(1, len(lista), 1):
    if(lista[i] > maior):
        maior = lista[i]
        posicao = i + 1

print("O maior valor encontrado foi: ", maior)
print("A posição que ele está é: ", posicao)
