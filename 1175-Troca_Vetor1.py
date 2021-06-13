index = []
x = []

for addIndex in range(0, 20, 1):
    index.append(addIndex)

for value in range(0, 20, 1):
    x.append(int(input()))

x.reverse()

for i, v in zip(index, x):
    print("N[%d] = %d" % (i, v))