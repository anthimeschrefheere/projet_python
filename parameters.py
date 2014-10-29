# -*- coding: utf8 -*-
def identify(name_1,name_2,i):
    print "saisissez le nom du joueur", i,":"
    name_1=raw_input()
    while name_1 == "" or name_1[0]==" " or name_1 == name_2: # ajoute les erreurs de type up_arrow
        name_1=raw_input("Entrer un nom valide ou un nom pas deja utilise : ")
    return name_1