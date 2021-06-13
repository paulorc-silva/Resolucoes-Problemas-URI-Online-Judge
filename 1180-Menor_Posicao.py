n = int(input())
x = []
val = input().split()

for item in val:
    x.append(int(item))

menor = x[0]
posicao = 0
    
for i in range(1, len(x), 1):
    if(x[i] < menor):
        menor = x[i]
        posicao = i 

print("Menor valor: %d" % menor)
print("Posicao: %d" % posicao)