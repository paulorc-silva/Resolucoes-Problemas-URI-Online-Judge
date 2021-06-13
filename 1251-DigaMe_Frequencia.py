from operator import itemgetter as ig

cont = 0

while(True):
    try:
        chars = input()
        
        if(cont > 0):
            print('')
            
        dicionario = {}

        for letra in chars:
            if(letra not in dicionario):
                dicionario[letra] = 1
            
            else:   
                dicionario[letra] += 1

        lista = []
        
        for k, v in dicionario.items():
            lista.append((k, v))

        lista.sort(key=ig(0), reverse=True)    
        lista.sort(key=ig(1))

        for val in lista:
            print(ord(val[0]), val[1])
            
        cont += 1
        
    except EOFError:
        break