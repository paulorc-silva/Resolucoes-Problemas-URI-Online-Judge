while(True):
    entrada = input().split()
    n, d = entrada
    n = int(n)
    d = int(d)

    if((n == 0) and (d == 0)):
        break

    n1 = n
    d1 = d
    num = input()
    pilha = []

    for i in num:
        pilha.append(i)
        while((len(pilha) > 1) and (pilha[-1] > pilha[-2]) and (d > 0)):
            pilha.pop(-2)
            d -= 1

    pilha = ''.join(pilha)
    if(len(pilha) > (n1 - d1)):
        pilha = (pilha[0:n1 - d1])
        
    print(pilha)