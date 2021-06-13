'''Minha solução - Wrong Answer 10%'''
while(True):
    n = int(input())
    
    if(n == 0):
        break

    x = input().split()

    posteQuebrado = 0
    soma = 0
    inicio = 0
    postes = 0
    
    for i in range(0, len(x), 1):
        x.insert(i, int(x[i]))
        x.pop(i + 1)

        if((x[0] == 0) and (x[1] == 0) and (x[2] == 1) and (x[-1] == 0)):
            pass

        else:
            if((x[i] == 0) and (inicio == 0)):
                posteQuebrado += 1
                postes += 1
                
            elif((x[i] == 0) and (inicio == 1)):
                postes += 1
                    
            if(x[i] == 1):
                inicio = 1
                soma += (postes / 2)
                soma = int(soma)
                postes = 0

    if(postes > 0):
        soma -= (posteQuebrado / 2)
        postes += posteQuebrado
        soma += (postes / 2)

    print("%d" % soma)

'''Solução do Otávio - Accepted'''
# n = int(input())

# while(n != 0):
#     x = list(map(int, input().split()))

#     if((x[0] == 0) and (x[1] == 0) and (x[2] == 1) and (x[-1] == 0)):
#         pass
#     else:
#         x.reverse()

#     cont = 0

#     for i in range(0, (n - 1), 1):
#         a = x[i - 1]
#         b = x[i]
#         c = x[i + 1]

#         if((a == 0) and (b == 0) and (c == 0)):
#             x[i] = 1
#             cont += 1
        
#         elif((a == 0) and (b == 0) and (c == 1)):
#             x[i - 1] = 1
#             cont += 1

#         elif((a == 1) and (b == 0) and (c == 0)):
#             x[i + 1] = 1
#             cont += 1

#     print(cont)

#     n = int(input())