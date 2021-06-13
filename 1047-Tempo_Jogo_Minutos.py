tempo = input().split()
hi, mi, hf, mf = tempo

hi = int(hi)
mi = int(mi)
hf = int(hf)
mf = int(mf)

inicio = (hi * 60) + mi
fim = (hf * 60) + mf
duracao = 0

if(hi <= hf):
    if(fim < inicio):
        duracao = inicio - fim
        print("O JOGO DUROU 23 HORA(S) E %d MINUTO(S)" % (60 - (duracao % 60)))
        
    else:
        duracao = fim - inicio
        
        if(duracao == 0):
            print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")
    
        else: 
            print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)" % ((duracao - (duracao % 60)) / 60, (duracao % 60)))

else:
    duracao = ((24 * 60) - inicio) + fim
    print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)" % ((duracao - (duracao % 60)) / 60, (duracao % 60)))