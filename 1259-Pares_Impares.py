n = int(input())
par = []
impar = []

for leitura in range(0, n, 1):
    num = int(input())
    
    if((num % 2) == 0):
        par.append(num)

    else:
        impar.append(num)

par.sort()
impar.sort(reverse=True)

for val in par:
    print(val)

for val in impar:
    print(val)