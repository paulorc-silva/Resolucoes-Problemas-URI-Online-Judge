qtd = 0
soma = 0

for cont in range(1, 7, 1):
    num = float(input("Digite um número positivo ou negativo: "))

    if(num > 0):
        soma += num
        qtd += 1
    
media = soma / qtd

print(qtd, "valores positivos")
print("A média dos números positivos é: %.1f" % media)