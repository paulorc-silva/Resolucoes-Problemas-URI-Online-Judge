from operator import itemgetter as ig

n = int(input())

while(True):    
    if(n == 0):
        break

    pessoas = []

    for i in range(0, n, 1):
        nome = input()
        infos = input().split()
        cor, tamanho = infos
    
        pessoa = tuple((cor, tamanho, nome))
        pessoas.append(pessoa)
        
    nome = sorted(pessoas, key=ig(2))
    tamanho = sorted(nome, key=ig(1), reverse=True)
    cor = sorted(tamanho, key=ig(0))

    for pessoa in range(0, len(pessoas), 1): 
        print('%s %s %s' % (cor[pessoa]))

    n = int(input())
    
    if(n != 0):
        print('')