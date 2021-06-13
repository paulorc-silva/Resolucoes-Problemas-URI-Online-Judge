n = int(input("Digite um número: "))

for cont in range(1, 10001, 1):
    if((cont % n) == 2):
        print(cont)