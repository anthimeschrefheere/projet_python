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

def somme(split,nombre,sommeo):
	somme=nombre.index(split[0])
	i=1
	while i<len(split):
		if split[i]!=split[i-1]:
			somme+=nombre.index(split[i])
		i+=1
	return somme

def egalite(split_1,split_2,nombre,somme_1,somme_2,nom_1,nom_2):
	somme_1=somme(split_1,nombre,somme_1)
	somme_2=somme(split_2,nombre,somme_2)
	if somme_1>somme_2:
		print nom_1, " est le vainqueur"
	elif somme_1<somme_2:
		print nom_2, " est le vainqueur"
	else:
		print "egalite parfaite"


def comparateur(ident_1,ident_2,split_1,split_2,nombre,somme_1,somme_2,nom_1,nom_2):
	i=0
	while ident_1[i]==ident_2[i]:
			i+=1
			if i>=min(len(ident_1),len(ident_2))-1:
				break
	if ident_1[i]>ident_2[i]:
		print nom_1, " est vainqueur"
	elif ident_2[i]>ident_1[i]:
		print nom_2, " est vainqueur"
	elif ident_1[i]==ident_2[i]:
		egalite(split_1,split_2,nombre,somme_1,somme_2,nom_1,nom_2)



