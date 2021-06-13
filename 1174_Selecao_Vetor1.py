a = []

for i in range(0, 100, 1):
    a.append(float(input()))

    if(a[i] <= 10):
        print("A[%d] = %.1f" % (i, a[i]))
