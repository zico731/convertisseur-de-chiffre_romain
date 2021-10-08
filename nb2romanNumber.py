decimal=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
romain=["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]


def conv_romain(chiffre):
    #assert chiffre >0 and chiffre< 4000, "le nombre saisi doit être compris entre 1 et 3999"
    chiffre0=chiffre
    
    i=0
    resultat =""
    while chiffre>0:
        if chiffre>=decimal[i]:
            resultat+=romain[i]
            chiffre-=decimal[i]
        else: 
            i += 1
    return chiffre0,resultat 

nb=1    
while nb !=0:
    nb=int(input("Entrez un nombre (0 = Quitter): "))
    if  0 < nb < 4000:
        print(conv_romain(nb))
    elif nb > 0:
        print ("le nombre saisi doit être compris entre 1 et 3999 !")
        
    print("")
