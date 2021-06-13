movimento = {'N': ['O', 'L'], 'L': ['N', 'S'], 'S': ['L', 'O'], 'O': ['S', 'N']}

while(True):
    numeros = input().split()
    n, m, s = numeros

    n = int(n)
    m = int(m)
    s = int(s)

    if((n == 0) and (m == 0) and (s == 0)):
        break

    aux = 0 
    direcao = ''
    matriz = []
    direcoes = ['N', 'S', 'O', 'L']
    pos_lin = None
    pos_col = None
    orientacao = None

    for lin_n in range(0, n, 1):
        linha = input()

        if((aux == 0) and any(direc in linha for direc in direcoes)):
            pos_col = [linha.find(direc) for direc in direcoes]
            pos_lin = lin_n

            for num in range(0, len(pos_col), 1):
                if(pos_col[num] != -1):
                    orientacao = direcoes[num]
                    pos_col = pos_col[num]
                    break

            aux = 1
        matriz.append(linha)

    instrucoes = input()
    pontuacao = 0

    for letra in instrucoes:
        if(letra == 'D'):
            orientacao = movimento[orientacao][1]

        elif(letra == 'E'):
            orientacao = movimento[orientacao][0]

        else:
            if((orientacao == 'N') and (pos_lin > 0)):
                if(matriz[pos_lin-1][pos_col] == '#'):
                    pass

                else:
                    pos_lin -= 1

            elif((orientacao == 'L') and (pos_col < (m - 1))):
                if(matriz[pos_lin][pos_col+1] == '#'):
                    pass
                
                else:
                    pos_col += 1

            elif((orientacao == 'S') and (pos_lin < (n - 1))):
                if(matriz[pos_lin+1][pos_col] == '#'):
                    pass

                else:
                    pos_lin += 1
            
            elif((orientacao == 'O') and (pos_col > 0)):
                if( matriz[pos_lin][pos_col-1] == '#'):
                    pass
 
                else:
                    pos_col -= 1

            if(matriz[pos_lin][pos_col] == '*'):
                pontuacao += 1
                i = pos_col
                matriz[pos_lin] = matriz[pos_lin][0:i] + '.' + matriz[pos_lin][i+1:]

    print(pontuacao)