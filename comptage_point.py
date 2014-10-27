def comptage(liste1,liste2):
	i=0
	j=0
	while j<len(liste1):
		if liste1[i]==liste1[j]:
			j+=1
		else:
			liste2.append(j-i)
			i=j
	liste2.append(j-i)

def somme(split,nombre,somme_x):
	somme=len(nombre[split[0]])
	i=1
	while i<len(split):
		if split[i]!=split[i-1]:
			somme+=len(nombre[split[i]])
		i+=1
	return somme_x

def egalite(split_1,split_2,nombre,somme_1,somme_2,nom_1,nom_2):
	somme_1=somme(split_1,nombre,somme_1)
	somme_2=somme(split_2,nombre,somme_2)
	if somme_1>somme_2:
		print nom_1, " est le vainqueur"
	elif somme_1<somme_2:
		print nom_2, " est le vainqueur"
	else:
		print "pure egalite"


def comparateur(ident_1,ident_2,nombre,somme_1,somme_2,nom_1,nom_2):
	i=0
	while i!=len(ident_1):
		if ident_1[i]==ident_2[i]:
			i+=1
		elif ident_1[i]>ident_2[i]:
			print nom_1, " est vainqueur"
			break
		elif ident_2[i]>ident_1[i]:
			print nom_2, " est vainqueur"
			break
	else:
		egalite(split_1,split_2,nombre,somme_1,somme_2,nom_1,nom_2)



def vainqueur(ident_1,ident_2,nombre,somme_1,somme_2,nom_1,nom_2):
	if len(ident_1)<=len(ident_2):
		comparateur(ident_1,ident_2,nombre,somme_1,somme_2,nom_1,nom_2)
	else:
		comparateur(ident_2,ident_1,nombre,somme_1,somme_2,nom_1,nom_2)
