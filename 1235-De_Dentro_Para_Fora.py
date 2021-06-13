n = int(input())

for leitura in range(0, n, 1):
    texto = input()
    
    centro = int(len(texto) / 2) - 1
    saida = texto[centro: :-1] + texto[(len(texto) - 1):centro:-1] 
    '''
        Slice [i:f:p], no caso abaixo será feito o seguinte:
        [centro:começo da string:-1], sendo que vai do centro até o começo da string, decrementando em 1
        Após isso, ele concatena com outro slice:
        [fim da string:centro:-1], sendo que vai do fim da string até o centro, decrementando em 1 
    '''
    print(saida) 