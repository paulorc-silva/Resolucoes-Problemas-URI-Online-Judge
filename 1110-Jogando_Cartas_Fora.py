while(True):
    n = int(input())

    if(n == 0):
        break

    inicio = []
    for i in range(1, (n + 1), 1):
        inicio.append(i)

    final = []
    while(len(inicio) > 1):
        final.append(int(inicio.pop(0)))
        inicio.append(int(inicio.pop(0)))

    print("Discarded cards: " + str(final).replace("[", "").replace("]", ""))
    print("Remaining card: " + str(inicio[0]))
