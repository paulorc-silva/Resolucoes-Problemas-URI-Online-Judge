x = int(input())
y = int(input())
soma = 0

if(x > y):
    for cont in range(y+1, x, 1):
        if((cont % 2) == 1):
            soma += cont

elif(x < y):
    for cont in range(x, y, 1):
        if((cont % 2) == 1):
            soma += cont

print(soma) 