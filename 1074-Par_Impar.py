qtd = int(input("Digite a quantidade de números: "))

for cont in range(0, qtd, 1):
    num = int(input("Digite um número: "))

    if(num == 0):
        print("NULL")

    elif(((num % 2) == 0) and (num > 0)):
        print("EVEN POSITIVE")

    elif(((num % 2) == 0) and (num < 0)):
        print("EVEN NEGATIVE")

    elif(((num % 2) != 0) and (num > 0)):
        print("ODD POSITIVE")

    elif(((num % 2) != 0) and (num < 0)):
        print("ODD NEGATIVE")