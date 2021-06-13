while(True):
    numeros = input().split()
    a, b = numeros

    a = int(a)
    b = int(b)

    if((a <= 0) or (b <= 0)):
        break

    soma = 0

    if(a < b):
        for seq in range(a, (b + 1), 1):
            soma += seq
            print(seq, end=' ')
        
        print("Sum=%d" % soma)

    else:
        for seq in range(b, (a + 1), 1):
            soma += seq
            print(seq, end=' ')
        
        print("Sum=%d" % soma)