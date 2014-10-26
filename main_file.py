# -*- coding: utf8 -*-
import parameters
import initialisation
import action
import decision
'''
import affichage_joueur
'''
nombre=['7','8','9','10','Valet','Dame','Roi','As']
figure=['trefle','carreau','coeur','pique']
liste=[]
joueur_1=[]
joueur_2=[]
defausse_1=[]
defausse_2=[]
pioche=[]
revealcard=[]
split_J1=[]
split_J2=[]
choix=""
JOUEUR1=""
JOUEUR2=""
nom_1=""
nom_2=""
nom_1=parameters.identify(nom_1,1)
nom_2=parameters.identify(nom_1,2)

print "______________________liste primaire____________________________"
initialisation.card_game(liste,nombre,figure)
print'_______________________debut melange_____________________________'
initialisation.Shuffle(liste)
print"_______________________fin melange_______________________________"
print"_______________________cartes melangees__________________________"
initialisation.distribution(liste,joueur_1,joueur_2,pioche)
print"_______________________cartes distribuees________________________"
pioche,JOUEUR1,JOUEUR2=initialisation.actif_player(pioche,nombre,JOUEUR1,JOUEUR2,nom_1,nom_2)
'''
affichage_joueur.affichage_joueur(joueur_1,choix)
affichage_joueur.affichage_joueur(joueur_2,choix)
'''
for i in range(4):
    print "tour", i+1
    pioche,revealcard=action.show_card (pioche,revealcard)
    decision.choice_card (JOUEUR1,JOUEUR2,revealcard,joueur_1,joueur_2,nom_1,nom_2)
    action.delete()
    decision.defausse(joueur_1,defausse_1,nom_1)
    action.delete()
    decision.defausse(joueur_2,defausse_2, nom_2)
    action.delete()
    JOUEUR1,JOUEUR2=action.turn_value(JOUEUR1,JOUEUR2)
print "joueur_1",joueur_1
print "joueur_2",joueur_2
print "defausse_1",defausse_1
print "defausse_2",defausse_2
print"____________________________partie treminee_____________________"
print"__________________________comptage des points_____________________"
action.split(joueur_1,split_J1)
action.split(joueur_2,split_J2)
print "split_J1", split_J1
print "split_J2", split_J2
