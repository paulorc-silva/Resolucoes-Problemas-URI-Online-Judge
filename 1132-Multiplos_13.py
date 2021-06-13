x = int(input())
y = int(input())
mult = 0

if(x < y):
    for cont in range(x, (y + 1), 1):
        if((cont % 13) != 0):
            mult += cont

else:
    for cont in range(y, (x + 1), 1):
        if((cont % 13) != 0):
            mult += cont

print(mult)