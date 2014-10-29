# -*- coding: utf8 -*-
import os

def split(liste1,liste2):
    for i in range(len(liste1)):
        valeur=liste1[i]
        valeur=valeur.split(";")
        liste2.append(valeur[0])
    return liste2
        
def show_card(liste1,liste2):
    liste2=liste1[0:4]
    liste1=liste1[4:]
    return liste1,liste2

def show_card2(liste1,liste2,liste3):
    liste3=liste1[0:2]+liste2[0:2]
    liste1=liste1[2:]
    liste2=liste2[2:]
    return liste1,liste2,liste3

def turn_value(i,j):
    i,j=j,i
    return i,j

def delete():
    trash=os.system('clear')

