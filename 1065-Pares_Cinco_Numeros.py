par = 0

for cont in range(1, 6, 1):
    num = float(input("Digite um número positivo ou negativo: "))

    if((num % 2) == 0):
        par += 1

print(par, "valores pares")