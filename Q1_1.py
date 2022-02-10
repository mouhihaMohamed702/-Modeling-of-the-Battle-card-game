
# 1.	Écrivez une fonction str_carte(carte) qui renvoie une chaîne contenant la représentation en toutes lettres de la carte passée en argument.
import random

def str_carte(c):
    return valeur.get(c[1])+" de "+c[0]

couleur = ('pique','coeur','carreau','trefle')
valeur = { 2: 'Deux', 3:'Trois', 4: 'Quatre', 5: 'Cinq', 6: 'Six',7: 'Sept', 8: 'Huit', 9: 'Neuf', 10: 'Dix',11: 'Valet', 12: 'Dame', 13: 'Roi', 14: 'As' }

c=('Pique',8)
print(str_carte(c))

