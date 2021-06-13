x = int(input())
n = [0] * 10

for i in range(0, len(n), 1):
    n[i] = x
    x *= 2
    print("N[%d] = %d" % (i, n[i]))