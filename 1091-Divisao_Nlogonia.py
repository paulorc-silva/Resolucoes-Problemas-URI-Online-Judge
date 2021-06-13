while(True):
    k = int(input())
    if(k == 0):
        break
    
    coordenadasPD = input().split()

    n, m = coordenadasPD
    n = int(n)
    m = int(m)

    for times in range(0, k, 1):
        coordenadasResidencia = input().split()

        x, y = coordenadasResidencia
        x = int(x)
        y = int(y)

        if((x == n) or (y == m)):
            print("divisa")

        elif((x < n) and (y > m)):
            print("NO")

        elif((x > n) and (y > m)):
            print("NE")

        elif((x > n) and (y < m)):
            print("SE")

        elif((x < n) and (y < m)):
            print("SO")
