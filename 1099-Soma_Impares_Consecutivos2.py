n = int(input())

for leituras in range(0, n, 1):
    numeros = input().split()
    x, y = numeros 
    x = int(x)
    y = int(y)
    soma = 0

    if(x > y):
        for cont in range(y+1, x, 1):
            if((cont % 2) == 1):
                soma += cont

    elif(x < y):
        for cont in range(x+1, y, 1):
            if((cont % 2) == 1):
                soma += cont

    print(soma)