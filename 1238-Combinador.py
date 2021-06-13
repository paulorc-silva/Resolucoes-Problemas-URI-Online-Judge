n = int(input())

for leitura in range(0, n, 1):
    frase = input().split()
    p1, p2 = frase
    nova_frase = ''

    if(len(p1) <= len(p2)):
        for i in range(0, len(p1), 1):
            nova_frase += p1[i]
            nova_frase += p2[i]
        nova_frase += p2[len(p1):]

    else:
        for i in range(len(p2)):
            nova_frase += p1[i]
            nova_frase += p2[i]
        nova_frase += p1[len(p2):]
        
    print(nova_frase)