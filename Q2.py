import random
couleur = ('pique','coeur','carreau','trefle')
valeur = { 2: 'Deux', 3:'Trois', 4: 'Quatre', 5: 'Cinq', 6: 'Six',7: 'Sept', 8: 'Huit', 9: 'Neuf', 10: 'Dix',11: 'Valet', 12: 'Dame', 13: 'Roi', 14: 'As' }
listJ1 =[]
listJ2 =[]

# supposon toujours que chaque joueur a 14 cartes
def jeu_de_carteJ1() :
    for i in range(14):
        rand_itemt = random.choice(couleur)
        rand_itemd = random.choice(list(valeur))
        tup =(rand_itemt,rand_itemd)
        listJ1.append(tup)
    return listJ1

def jeu_de_carteJ2() :
    for i in range(14):
        rand_itemt = random.choice(couleur)
        rand_itemd = random.choice(list(valeur))
        tup =(rand_itemt,rand_itemd)
        listJ2.append(tup)
    return listJ2

jeu_de_carteJ1()
jeu_de_carteJ2()


def jeu(listJ1,listJ2):
    j1=0
    j2=0
    for i in range(14):
        print(" round {}".format(i+1))
        tup1=listJ1[i]
        tup2=listJ2[i]
        if tup1[1]<tup2[1]:
            j2=j2+1

            print("le joueur 1 jeu {} et le joueur 2 jeu {} est le gagnant est joueur 2 ".format(listJ1[i],listJ2[i]))
        elif tup1[1]==tup2[1]:
            print("le joueur 1 jeu {} et le joueur 2 jeu {} sont eagu".format(listJ1[i], listJ2[i]))
        else :
            j1 = j1 + 1
            print("le joueur 1 jeu {} et le joueur 2 jeu {} est le gagnant est joueur 1".format(listJ1[i], listJ2[i]))

        if(j1>j2):

            t = (j1, j2,1)
        elif (j1==j2):
            t = (j1, j2, "sont egau")
        else :
            t = (j1, j2, 2)

    return t


print('le joueur 1 a eu {} points et le joueur 2 a eu {} points et le joueur qui gagne est {}'
      .format(jeu(listJ1,listJ2)[0],jeu(listJ1,listJ2)[1],jeu(listJ1,listJ2)[2]))







