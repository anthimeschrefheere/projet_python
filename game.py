import action
import decision

def simple(pioche,JOUEUR1,JOUEUR2,revealcard,joueur_1,joueur_2,nom_1,nom_2,defausse_1,defausse_2):
	joueur_1.sort()
	joueur_2.sort()
	pioche,revealcard=action.show_card (pioche,revealcard)
	decision.choice_card (JOUEUR1,JOUEUR2,revealcard,joueur_1,joueur_2,nom_1,nom_2)
	action.delete()
	joueur_1.sort()
	joueur_2.sort()
	decision.defausse(joueur_1,defausse_1,nom_1)
	action.delete()
	decision.defausse(joueur_2,defausse_2, nom_2)
	action.delete()
	JOUEUR1,JOUEUR2=action.turn_value(JOUEUR1,JOUEUR2)
	return JOUEUR1,JOUEUR2,revealcard,joueur_1,joueur_2,defausse_1,defausse_2

def avancee(revealcard,defausse_1,defausse_2,JOUEUR1,JOUEUR2,nom_1,nom_2):
	joueur_1.sort()
	joueur_2.sort()
	defausse_1,defausse_2,revealcard=action.show_card2(defausse_1,defausse_2,revealcard)
	decision.choice_card (JOUEUR1,JOUEUR2,revealcard,joueur_1,joueur_2,nom_1,nom_2)
	action.delete()
	joueur_1.sort()
	joueur_2.sort()
	decision.defausse(joueur_1,defausse_1,nom_1)
	action.delete()
	decision.defausse(joueur_2,defausse_2, nom_2)
	action.delete()
	JOUEUR1,JOUEUR2=action.turn_value(JOUEUR1,JOUEUR2)
	return revealcard,defausse_1,defausse_2,JOUEUR1,JOUEUR2,nom_1,nom_2