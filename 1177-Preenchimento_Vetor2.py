t = int(input())
n = []

for i in range(0, 1000, 1):
    for num in range(0, t, 1):
        n.append(num)
        num += 1 

    print("N[%d] = %d" % (i, n[i]))