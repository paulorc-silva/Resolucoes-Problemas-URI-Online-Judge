x = []

for i in range(0, 10, 1):
    x.append(int(input()))

    if(x[i] <= 0):
        x[i] = 1
        print("X[%d] = %d" % (i, x[i]))

    else:
        print("X[%d] = %d" % (i, x[i])) 