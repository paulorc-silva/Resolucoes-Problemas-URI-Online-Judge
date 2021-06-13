from operator import itemgetter as ig

def classificacao_final(n, cont):
    response ={}

    for leitura in range(0, int(n*(n-1)/2), 1):
        x, y, z, w = map(int, input().split())

        pts_feito_x = y
        pts_tomado_x = w

        pts_feito_z = w
        pts_tomado_z = y

        if(y > w):
            vit_x = 2
            vit_z = 1

        else:
            vit_x = 1
            vit_z = 2

        if(x not in response):
            response[x] = [x, vit_x, 0, pts_feito_x, pts_tomado_x]

        else:
            response[x][1] += vit_x
            response[x][3] += pts_feito_x 
            response[x][4] += pts_tomado_x
            
        if(z not in response):
            response[z] = [z, vit_z, 0, pts_feito_z, pts_tomado_z]
        
        else:
            response[z][1] += vit_z
            response[z][3] += pts_feito_z 
            response[z][4] += pts_tomado_z

    response1 = []

    for k, v in response.items():
        response1.append(v)

    for i in response1:
        if(i[4] == 0):
            i[2] = i[3]

        else:
            i[2] = i[3] / i[4]
   
    response2 = sorted(response1.copy(), key=ig(0))
    response3 = sorted(response2.copy(), key=ig(3), reverse = True)
    response4 = sorted(response3.copy(), key=ig(2), reverse = True)
    response5 = sorted(response4.copy(), key=ig(1), reverse = True)

    print('Instancia', cont)
    
    for i in range(0, len(response5)-1, 1):
        print(response5[i][0], end = ' ')

    print(response5[-1][0])
  
 
cont = 0
n = int(input())

while(n != 0):
    if(cont == 0):
        cont += 1
        classificacao_final(n, cont)
    
    else:
        print()
        cont += 1
        classificacao_final(n, cont)
    
    n = int(input())