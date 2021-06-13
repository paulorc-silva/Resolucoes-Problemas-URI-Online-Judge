vertebra = input("Digite se o animal é vertebrado ou invertebrado: ")
classe = input("Digite a classe do animal (Ex.: ave, mamifero, inseto etc): ")
alimento = input("Digite o tipo de alimentação do animal (Ex.: onivoro, carnivoro, herbivoro etc): ")

if(vertebra == "vertebrado"):
    if(classe == "ave"):
        if(alimento == "carnivoro"):
            print("aguia")
        
        else:
            print("pomba")
    
    else:
        if(alimento == "onivoro"):
            print("homem")
        
        else:
            print("vaca")

else:
    if(classe == "inseto"):
        if(alimento == "hematofago"):
            print("pulga")
        
        else:
            print("lagarta")

    else:
        if(alimento == "hematofago"):
            print("sanguessuga")
        
        else:
            print("minhoca")
    