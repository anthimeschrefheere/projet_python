# -*- coding: utf8 -*-
import help
import action

def  nom_jeux():
	print"____________________________________________"
	print"         le double carre                    "
	print"____________________________________________"
	print"entrer 1 pour commencer le jeux"
	print"entrer une autre valeur pour voir l'aide complete"
	erreur=1
	while erreur:
		erreur=0
		try:
			decision=int(raw_input("choix:"))
		except ValueError:
			print "veuillez entrer un nombre valide"
			erreur=1
		if decision!=1:
			help.general()

def choix_mode(advance):
	print "choix du style de jeux:"
	print "1 pour jeux simple en 4 tours"
	print "2 pour jeux avance en 8 tours"
	print "autre nombre pour l aide entre les 2 styles"
	erreur=1
	while erreur:
		erreur=0
		try:
			advance=int(raw_input("choix:"))
		except ValueError:
			print "veuillez entrer un nombre valide"
			erreur=1
		if advance!=1 and advance!=2:
			help.aide_deux_modes()
			erreur=1
	return advance

def choix_help(nom):
	print nom
	print"selectionner 1 pour continuer le jeu"
	print"selectionner un autre nombre pour demander l aide"
	erreur=1
	while erreur:
		erreur=0
		try:
			choix=int(raw_input("choix:"))
		except ValueError:
			print "veuillez entrer un nombre valide"
			erreur=1
		if choix!=1:
			help.aide_choix_joueur()
			erreur=1

def debut_tour():
	print"appuyer sur 1 pour debuter le jeu"
	erreur=1
	while erreur:
		erreur=0
		try:
			x=int(raw_input("choix:"))
		except ValueError:
			print "veuillez entrer un nombre valide"
			erreur=1
	action.delete()

def affichage(liste1):
	for i in range(len(liste1)):
		print i+1 , " : ", liste1[i]