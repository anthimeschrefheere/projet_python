# -*- coding: utf8 -*-
def choice_card1(liste1,liste2,i):
    print i," choisissez quelle carte tirer entre 1 et ", len(liste1)
    choix=input()
    carte_tire=liste1[choix-1]
    valeur_carte=carte_tire.split(";")
    valeur_carte=liste2.index(valeur_carte[0])
    return carte_tire,valeur_carte

def choice_card2(JOUEUR1,JOUEUR2,liste1,liste2,liste3,nom):
    print "le joueur actif est", nom
    print "les cartes sont",liste1
    print "choisissez une carte endonnant sa position dans la liste entre 1 et ",len(liste1)
    choix=input("choix:")
    liste2.append(liste1[choix-1])
    print"vous avez choisi la carte", liste1[choix-1]
    liste1.remove(liste1[choix-1])
    print"les cartes restantes sont ", liste1
    print "choisissez une carte en donnant sa position dans la liste entre 1 et ",len(liste1)
    choix=input("choix:")
    liste2.append(liste1[choix-1])
    print"vous avez choisi la carte", liste1[choix-1]
    liste1.remove(liste1[choix-1])
    liste3.append(liste1[0])
    liste3.append(liste1[1])
    liste1=[]
    return liste1,liste2,liste3

def choice_card (JOUEUR1,JOUEUR2,liste1,liste2,liste3,nom_1,nom_2):
    if JOUEUR1>JOUEUR2:
        choice_card2(JOUEUR1,JOUEUR2,liste1,liste2,liste3,nom_1)
    else:
        choice_card2(JOUEUR2,JOUEUR1,liste1,liste3,liste2,nom_2)
    return liste1,liste2,liste3

def defausse(liste1,liste2,nom):
    print "tour de ", nom
    print liste1
    print "donnez la position des deux cartes a defausser une carte entre 1 et 10"
    choix1=input("choix 1:")
    choix2=input("choix 2:")
    while choix1==choix2:
        print "vous avez selectionne deux fois la meme carte, veuillez recommencer"
        choix2=input("choix 2:")
    liste2.append(liste1[choix1-1])
    liste2.append(liste1[choix2-1])
    liste1.remove(liste1[choix1-1])
    if choix1<choix2:
        liste1.remove(liste1[choix2-2])
    else:
        liste1.remove(liste1[choix2-1])
    return liste1,list