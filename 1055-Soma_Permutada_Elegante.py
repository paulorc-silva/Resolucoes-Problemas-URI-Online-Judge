c = 1
t = int(input())

while(t > 0):
    t -= 1

    s = input().split()
    n = int(s[0])
    x = [int(j) for j in s[1:]]
    x.sort()

    a = x[0]
    b = x[n-1]
    r = b - a
    i = 1
    j = n - 2

    while(i < j):
        r += x[j] - a + b - x[i]
        a = x[i]
        b = x[j]
        i += 1
        j -= 1

    if(i == j):
        if((x[i] - a) > (b - x[i])):
            r += x[i] - a

        else:
            r += b - x[i]

    print("Case %d: %d" % (c, r))
    c += 1