n = int(input("Digite a quantidade de números: "))
dentro = 0
fora = 0

for cont in range(0, n, 1):
    x = int(input("Digite um número: "))

    if((x >= 10) and (x <= 20)):
        dentro += 1
    
    else:
        fora += 1

print(dentro, "in")
print(fora, "out")