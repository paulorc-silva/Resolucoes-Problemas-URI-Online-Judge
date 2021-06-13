n = int(input())

for leitura in range(0, n, 1):
    chars = input()

    if(chars[0] == chars[2]):
        resposta = int(chars[0]) * int(chars[2])

    else:
        if(chars[1].isupper()):
            resposta = int(chars[2]) - int(chars[0])

        elif(chars[1].islower()):
            resposta = int(chars[0]) + int(chars[2])

    print(resposta)