while(True):
    try:
        n = int(input())
        v = []
        c = 0 
        
        if(n <= 0):
            break
        
        for leitura in range(0, n, 1):
            s = input()
            v.append(s)
        
        v.sort()
        base = v[0] 
        l = len(base)
            
        for i in range(1, n, 1):
            for j in range(0, l, 1):
                if(base[j] == v[i][j]):
                    c += 1
                    
                else:
                    break 
            
            base = v[i]

        print('%d\n' % c)
    
    except EOFError:
        break
    
    
