# -*- coding: utf8 -*-
def value():
	nombre=['7','8','9','10','Valet','Dame','Roi','As']
	figure=['trefle','carreau','coeur','pique']
	#Player_1=[joueur_1,defausse_1,split_J1,ident_1] future liste contenant les infos de Player_1
	#Player_2=[joueur_2,defausse_2,split_J2,ident_2] future liste contenant les infos de Player_2
	liste=[]
	joueur_1=[]
	joueur_2=[]
	defausse_1=[]
	defausse_2=[]
	pioche=[]
	revealcard=[]
	split_J1=[]
	split_J2=[]
	ident_1=[]
	ident_2=[]
	choix=""
	JOUEUR1=""
	JOUEUR2=""
	nom_1=""
	nom_2=""
	somme_1=""
	somme_2=""
	advance=0
	return choix,JOUEUR1,JOUEUR2,nom_1,nom_2,somme_1,somme_2,advance

def identify(name_1,name_2,i):
    print "saisissez le nom du joueur", i,":"
    name_1=raw_input()
    while name_1 == "" or name_1[0]==" " or name_1 == name_2: # ajoute les erreurs de type up_arrows
        name_1=raw_input("Entrer un nom valide ou un nom pas deja utilise : ")
    return name_1