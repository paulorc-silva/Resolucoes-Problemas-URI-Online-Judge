def merge_sort(v, n):
    temp_v = [0] * n
    
    return inversion_count(v, temp_v, 0, n-1) 
    
    
def inversion_count(v, temp_v, esquerda, direita):
    ic = 0
    
    if(esquerda < direita):
        meio = (esquerda + direita) // 2
        
        ic += inversion_count(v, temp_v, esquerda, meio)
        ic += inversion_count(v, temp_v, meio+1, direita)
        ic += merge(v, temp_v, esquerda, meio, direita)
        
    return ic
        
        
def merge(v, temp_v, esquerda, meio, direita):
    i = esquerda
    j = meio + 1
    k = esquerda
    ic = 0
    
    while((i <= meio) and (j <= direita)):
        if(v[i] <= v[j]):
            temp_v[k] = v[i] 
            k += 1
            i += 1
        
        else:
            temp_v[k] = v[j]
            ic += (meio - i + 1)
            k += 1
            j += 1
    
    while(i <= meio):
        temp_v[k] = v[i] 
        k += 1
        i += 1
        
    while(j <= direita):
        temp_v[k] = v[j] 
        k += 1
        j += 1
            
    for copy_sort in range(esquerda, (direita + 1), 1):
        v[copy_sort] = temp_v[copy_sort]
        
    return ic
    
    
n = int(input())

for leitura in range(0, n, 1):
    l = int(input())
    vagao = list(map(int, input().split()))

    tam_v = len(vagao)
    ic = merge_sort(vagao, tam_v)
    
    print('Optimal train swapping takes %d swaps.' % ic)