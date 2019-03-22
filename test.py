# coding: utf-8

import re

def premier_test(chaine):
    # Cette fonction d'effectuer un premier test de l'equation recue.
    #r"^( )?(([0-9]+)( \* X\^0)?( - | \+ )?)?(([0-9]+)( \* X\^1| \* X)( - | \+ )?)?( )?$?(([0-9]+)( \* X\^2))"
    motif_1 = r"^( )?(([0-9]+)( \* X\^0)?( - | \+ )?)?(([0-9]+)( \* X\^1| \* X)( - | \+ )?)?(([0-9]+)( \* X\^2))?( )?"
    for element in chaine:
        if re.match(motif_1, element):
            continue
        else:
            print("Please enter a valid equation 1 !")
            exit()

def tests_elementaires(chaine):
    # Cette fonction d'effectuer un test elementaire de l'equation recue.
    for i, element in enumerate(chaine):
        if element == 'X^0' or element == 'X^1' or element == 'X':
            if i + 1 != len(chaine) and chaine[i+ 1] not in '+-':
                print("Please enter a valid equation !")
                exit()
    
    if len(chaine) >= 2 and chaine[1] != 'X^0' and chaine[1] != 'X^1' and chaine[1] != 'X':
        if chaine[1] != '*' and chaine[1] != '-' and chaine[1] != '+':
            print("Please enter a valid equation !")
            exit()

def second_test(chaine):
    # Cette fonction d'effectuer un deuxieme test de l'equation recue.
    gauche = chaine[0].split()
    droite = chaine[1].split()
    tests_elementaires(gauche)
    tests_elementaires(droite)
    