qtd = int(input())

for i in range(0, qtd, 1):
    heroes = input().split()

    nome, forca = heroes
    forca = int(forca)

    if(nome == "Thor"):
        print("Y")
    
    else:
        print("N")