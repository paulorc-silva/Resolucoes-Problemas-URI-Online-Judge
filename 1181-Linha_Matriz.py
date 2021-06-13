l = int(input())
t = input()
m = []

for i in range(0, 12, 1):
    m.append([])

for i in range(0, 12, 1):
    for j in range(0, 12, 1):
        x = float(input())
        m[i].append(x)
        
if(t == 'S'):
    soma = 0

    for k in m[l]:
        soma += k

    print(soma)

if(t == 'M'):
    med = 0
    soma = 0

    for k in m[l]:
        soma += k
        
    med = soma/12
    print(med)