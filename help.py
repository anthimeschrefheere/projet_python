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

def aide_deux_modes():
    print"aide concernant les 2 styles de jeu"
    print"jeu simple en 4 tours:"
    print"le jeu se deroule en 4 tours"
    print"a chaque tour le joueur actif choisi 2 cartes dans les 4 cartes de la pioche revelee"
    print" le joueur non actif recoit les 2 cartes restantes"
    print"chaque joueur jette ensuite de son jeu, 2 cartes face cachee"
    print"le joueur non actif devient le joueur actif au tour suivant"
    print"jeu avancee en 8 tours:"
    print"les 4 premiers tours se deroule de la meme maniere que le jeu simple"
    print"chaque joueur defausse ces cartes dans une defausse personnelle qu il peut a tout moment afficher"
    print"pour les tours 5 a 8:"
    print"la defausse se fait normalement"
    print"les cartes revelees viennent des defausses des joueurs"
    print"chaque joueur revele les deux premieres cartes de sa defausse"
    print"le joueur actif selectionne 2 cartes le joueur non actif recuperant les cartes restantes"
    print"a chaque tour on interverti le joeur actif et non actif"
    print" les regles pour determiner le vainqueur sont identiques"

def aide_choix_joueur():
    print"ce tour sert a choisir lequel des joueurs demarre en premier"
    print"veuillez tirer au sort une des 16 cartes de la pioche"
    print"differente du joueur 1"
    print"la carte sera ensuite remise dans la pioche par l'ordinateur"
    print"les cartes de la pioche seront ensuite melangees"

def comptage():
    print"_______________________________"
    print"      aide comptage des points "
    print"_______________________________"
    print" "
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
    print" "
    print" "
    print"en cas d egalite"
    print"la main la plus forte est la main avec le plus de point"
    print"compte des points"
    print"a chaque nombre est associé une valeur"
    print"0 point pour 7"
    print"7 points pour As"
    print"on ne garde qu'une seule carte par type de carte"
    print"puis on fait la somme des points des cartes gardees"
    print"si egalite des points la partie est nulle"
