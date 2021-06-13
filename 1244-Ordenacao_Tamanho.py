n = int(input())

for leitura in range(0, n, 1):
    texto = input().split()
    texto.sort(key = len, reverse = True)
    
    for i in range(0, len(texto), 1):
        print(texto[i], end = '')

        if(i != (len(texto) - 1)):
            print(' ', end = '')

    print()