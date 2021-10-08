decimal=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
romain=["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]


def conv_romain(chiffre):
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
for nb in range (1,4000):
    print(conv_romain(nb))
    print()    