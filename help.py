# -*- coding: utf8 -*-
def general():
    print"_______________________________"
    print"       aide complete           "
    print"_______________________________"


def principe():
    print"_______________________________"
    print"       principe du jeu         "
    print"_______________________________"
    print"materiel recquis:un jeu de 32 cartes"
    print"8 cartes sont distribuees a chaque joueur"


def deroulement():
    print"_______________________________"
    print"        deroulement du jeu     "
    print"_______________________________"
    

def comptage():
    print"_______________________________"
    print"      aide comptage des points "
    print"_______________________________"
    print"A a une main plus forte que B si la main de A posse le plus grand nombre de valeurs identiques"
    print"exemple:"
    print"main de A: 4*7,1*8, 1*9,1*10,1*Valet"
    print"main de B: 3*As, 3*Roi, 2*Dame"
    print"main de A gagne"
    print" "
    print" "
    print"main de A: 3*7, 3*8, 2*9"
    print"main de B: 3*As, 3*Roi,1*Valet, 1*Valet"
    print"main de A gagne"
    print"en cas d egalite"
    print"la main la plus forte est la main avec le plus de point"
    print"compte des points"
    print"a chaque nombre est associé une valeur"
    print"0 point pour 7"
    print"7 points pour As"
    print"on ne garde qu'une seule carte par type de carte"
    print"puis on fait la somme des points des cartes gardees"
    print"si egalite des points la partie est nulle"
