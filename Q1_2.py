import random

couleur = ('pique','coeur','carreau','trefle')
valeur = { 2: 'Deux', 3:'Trois', 4: 'Quatre', 5: 'Cinq', 6: 'Six',7: 'Sept', 8: 'Huit', 9: 'Neuf', 10: 'Dix',11: 'Valet', 12: 'Dame', 13: 'Roi', 14: 'As' }

listJ = []
def jeu_de_carte() :
    for i in range(14):
        rand_itemt = random.choice(couleur)
        rand_itemd = random.choice(list(valeur))
        tup =(rand_itemt,rand_itemd)
        listJ.append(tup)
    return listJ


print(jeu_de_carte())