t = int(input())

for i in range(0, t, 1):
    x = int(input())
    f = [0,1]
    if(x > 1):
        for j in range(2, (x + 1), 1):         
            f.append(f[j-2]+f[j-1])

        print('Fib(%d) = %d' % (x, f[x]))

    if(x <= 1):
        print('Fib(%d) = %d' % (x, f[x]))