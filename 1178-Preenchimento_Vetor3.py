x = float(input())

n = []
n.append(x)

for i in range(0, 100, 1):
    n.append(n[i] / 2)
    print("N[%d] = %.4f" % (i, n[i]))
