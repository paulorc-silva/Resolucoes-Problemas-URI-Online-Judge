n = int(input())

for leitura in range(0, n, 1):
    numeros = input().split()
    x, y = numeros

    x = int(x)
    y = int(y)

    if(y == 0):
        print("divisao impossivel")
    
    else:
        div = x / y
        
        print("%.1f" % div)