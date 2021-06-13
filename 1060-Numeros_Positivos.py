add = 0

for cont in range(1, 7, 1):
    num = float(input("Digite um número positivo ou negativo: "))

    if(num > 0):
        add += 1

print(add, "valores positivos")