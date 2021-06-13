n = int(input())

for leitura in range(0, n, 1):
    x = int(input())
    divisores = 0

    for nums in range(1, (x + 1), 1):
        if((x % nums) == 0):
            divisores += 1

    if(divisores == 2):
        print("%d eh primo" % x) 

    else:
        print("%d nao eh primo" % x) 