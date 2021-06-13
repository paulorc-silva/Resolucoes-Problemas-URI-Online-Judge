while(True):
    numCartas = input().split()

    a, b = numCartas
    a = int(a)
    b = int(b)

    if((a == 0) and ( b== 0)):
        break

    ca = [int(x) for x in input().split()]
    cb = [int(x) for x in input().split()]

    a = set(ca)
    b = set(cb)
    c = {}

    if(len(a) < len(b)):
        c = a
        a = b

    c = [x for x in c if x not in a]
    print(len(c))