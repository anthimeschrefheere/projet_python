# -*- coding: utf8 -*-
from random import Random
import decision
generateur=Random()

def card_game(liste1,liste2,liste3):
    carte=()
    for i in range(len(liste2)):
        for j in range(len(liste3)):
            carte=(liste2[i]+";"+liste3[j])
            liste1.append(carte)
    return liste1,liste2

def Shuffle(liste):
    generateur.shuffle(liste)
    return liste

def distribution(liste1,liste2,liste3,liste4):
    for i in range(len(liste1)):
        if i%2==0 and i<16:
            liste2.append(liste1[i])
        elif i%2==1 and i<16:
            liste3.append(liste1[i])
        else:
            liste4.append(liste1[i])
    return liste2,liste3,liste4

def actif_player(liste1,liste2,valeur_carte_j1,valeur_carte_j2,i,j):
    while 1:
        carte_tire_j1,valeur_carte_j1=decision.choice_card1(liste1,liste2,i)
        carte_tire_j2,valeur_carte_j2=decision.choice_card1(liste1,liste2,j)
        while valeur_carte_j1==valeur_carte_j2:
            print"la valeur est identique veuillez retirer les cartes"
            carte_tire_j2,valeur_carte_j2=decision.choice_card1(liste1,liste2,j)
        else:
            break
    print i," a tire la carte",carte_tire_j1, "avec la valeur de", valeur_carte_j1
    print j," a tire la carte",carte_tire_j2, "avec la valeur de", valeur_carte_j2
    if valeur_carte_j2<valeur_carte_j1:
        print i," est le joueur actif"
    else:
        print j," est le joueur actif"
    Shuffle(liste1)
    return(liste1,valeur_carte_j1,valeur_carte_j2)

