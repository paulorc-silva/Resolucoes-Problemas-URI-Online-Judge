n = int(input())

for leitura in range(0, n, 1):
    a, b = input().split()

    if(len(a) < len(b)):
        print('nao encaixa')
    
    else:
        if(a[(len(a) - len(b)):] == b): # Slice [i:f:p], no caso [a[i]: fim da string]
            print('encaixa')
    
        else:
            print('nao encaixa')