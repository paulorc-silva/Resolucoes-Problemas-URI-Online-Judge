x = int(input("Digite um número: "))

for impar in range(x, (x + 12), 1):
    if((impar % 2) != 0):
        print(impar)