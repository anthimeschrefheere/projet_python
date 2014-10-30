# -*- coding: utf8 -*-
import initialisation

def choice_card1(liste1,liste2,i):
    print i," choisissez quelle carte tirer entre 1 et ", len(liste1)
    erreur=1
    while erreur:
        erreur=0
        try:
            choix=int(raw_input())
            carte_tire=liste1[choix-1]
        except ValueError:
            print "veuillez entrer un nombre valide"
            erreur=1
        except IndexError:
            print "veuillez entrer un nombre compris entre 1 et 16"
            erreur=1
        if choix==0:
            print "veuillez entrer un nombre compris entre 1 et 16"
            erreur=1
    valeur_carte=carte_tire.split(";")
    valeur_carte=liste2.index(valeur_carte[0])
    return carte_tire,valeur_carte

def choice_card2(JOUEUR1,JOUEUR2,liste1,liste2,liste3,nom):
    print "le joueur actif est", nom
    print "les cartes sont",liste1
    print "choisissez une carte endonnant sa position dans la liste entre 1 et ",len(liste1)
    erreur=1
    while erreur:
        erreur=0
        try:
            choix=int(raw_input())
            carte_tire=liste1[choix-1]
        except ValueError:
            print "veuillez entrer un nombre valide"
            erreur=1
        except IndexError:
            print "veuillez entrer un nombre compris entre 1 et ",len(liste1)
            erreur=1
        if choix==0:
            print "veuillez entrer un nombre compris entre 1 et ", len(liste1)
            erreur=1
    liste2.append(liste1[choix-1])
    print"vous avez choisi la carte", liste1[choix-1]
    liste1.remove(liste1[choix-1])
    print"les cartes restantes sont ", liste1
    print "choisissez une carte en donnant sa position dans la liste entre 1 et ",len(liste1)
    erreur=1
    while erreur:
        erreur=0
        try:
            choix=int(raw_input())
            carte_tire=liste1[choix-1]
        except ValueError:
            print "veuillez entrer un nombre valide"
            erreur=1
        except IndexError:
            print "veuillez entrer un nombre compris entre 1 et ",len(liste1)
            erreur=1
        if choix==0:
            print "veuillez entrer un nombre compris entre 1 et ", len(liste1)
            erreur=1
    liste2.append(liste1[choix-1])
    print"vous avez choisi la carte", liste1[choix-1]
    liste1.remove(liste1[choix-1])
    liste3.append(liste1[0])
    liste3.append(liste1[1])
    liste1=[]
    return liste1,liste2,liste3

def choice_card (JOUEUR1,JOUEUR2,liste1,liste2,liste3,nom_1,nom_2):
    if JOUEUR1>JOUEUR2:
        print "liste de ", nom_1," : "
        initialisation.affichage(liste2)
        choice_card2(JOUEUR1,JOUEUR2,liste1,liste2,liste3,nom_1)
    else:
        print "liste de ", nom_2," : "
        initialisation.affichage(liste3)
        choice_card2(JOUEUR2,JOUEUR1,liste1,liste3,liste2,nom_2)
    return liste1,liste2,liste3

def defausse(liste1,liste2,nom): 
    print "tour de ", nom
    initialisation.affichage(liste1)
    print "donnez la position des deux cartes a defausser une carte entre 1 et 10"
    erreur=1
    while erreur:
        erreur=0
        try:
            print "choix1"
            choix1=int(raw_input())
            carte_tire=liste1[choix1-1]
        except ValueError:
            print "veuillez entrer un nombre valide"
            erreur=1
        except IndexError:
            print "veuillez entrer un nombre compris entre 1 et ",len(liste1)
            erreur=1
        if choix1==0:
            print "veuillez entrer un nombre compris entre 1 et ", len(liste1)
            erreur=1
    erreur=1
    while erreur:
        erreur=0
        try:
            print "choix2"
            choix2=int(raw_input())
            carte_tire=liste1[choix2-1]
        except ValueError:
            print "veuillez entrer un nombre valide"
            erreur=1
        except IndexError:
            print "veuillez entrer un nombre compris entre 1 et ",len(liste1)
            erreur=1
        if choix2==0:
            print "veuillez entrer un nombre compris entre 1 et ", len(liste1)
            erreur=1
    while choix1==choix2:
        print "vous avez selectionne deux fois la meme carte, veuillez recommencer"
        erreur=1
        while erreur:
            erreur=0
            try:
                print "choix2"
                choix2=int(raw_input())
                carte_tire=liste1[choix2-1]
            except ValueError:
                print "veuillez entrer un nombre valide"
                erreur=1
            except IndexError:
                print "veuillez entrer un nombre compris entre 1 et ",len(liste1)
                erreur=1
            if choix2==0:
                print "veuillez entrer un nombre compris entre 1 et ", len(liste1)
                erreur=1
    liste2.append(liste1[choix1-1])
    liste2.append(liste1[choix2-1])
    liste1.remove(liste1[choix1-1])
    if choix1<choix2:
        liste1.remove(liste1[choix2-2])
    else:
        liste1.remove(liste1[choix2-1])
    return liste1,list
