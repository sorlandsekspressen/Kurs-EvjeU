import numpy as np

#program 1 - med "manuell opptelling"

antall = 100

liste_terningkast=[]

for i in range(antall):
    tall = np.random.randint(1,7)
    liste_terningkast.append(tall)

antallEn = 0
antallTo = 0
antallTre = 0
antallFire = 0
antallFem = 0
antallSeks = 0

for x in liste_terningkast:
    if x == 1:
        antallEn = antallEn + 1
    elif x == 2:
        antallTo = antallTo + 1
    elif x == 3:
        antallTre = antallTre + 1
    elif x == 4:
        antallFire = antallFire + 1
    elif x == 5:
        antallFem = antallFem + 1
    elif x == 6:
        antallSeks = antallSeks + 1 
        
print("Enere:", antallEn)
print("Toere:", antallTo)
print("Treere:", antallTre)
print("Firere:", antallFire)
print("Femmere:", antallFem)
print("Seksere:", antallSeks)

#program 2 - med "count-funksjon"

antall = 100

liste_terningkast=[]

for i in range(antall):
    tall = np.random.randint(1,7)
    liste_terningkast.append(tall) 


antallEn = liste_terningkast.count(1)
antallTo = liste_terningkast.count(2)
antallTre = liste_terningkast.count(3)
antallFire = liste_terningkast.count(4)
antallFem = liste_terningkast.count(5)
antallSeks = liste_terningkast.count(6)

print("Enere:", antallEn)
print("Toere:", antallTo)
print("Treere:", antallTre)
print("Firere:", antallFire)
print("Femmere:", antallFem)
print("Seksere:", antallSeks)
            
#program 3 - komprimert med nøstet loop

antall = 10000

liste_resultat2 = [0,0,0,0,0,0]

for i in range(antall):
    tall = np.random.randint(1,7)
    for ii in range(1,7):
        if tall == ii:
            liste_resultat2[ii-1] += 1
        

