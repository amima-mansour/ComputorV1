# coding: utf-8

import re

def premier_test(chaine):
    # Cette fonction d'effectuer un premier test de l'equation recue.
    
    motif_1 = r"^( )?(-)?([0-9]*)(\.[0-9]+)?( \* )?(X\^([0-9])([0-9]*)|X|)(( - | \+ )([0-9]*)(\.[0-9]+)?( \* )?(X\^([0-9])([0-9]*)|X|))*( )?$"
    for element in chaine:
        if re.match(motif_1, element):
            continue
        else:
            print("Please enter a valid equation !")
            exit()

def tests_elementaires(chaine):
    # Cette fonction d'effectuer un test elementaire de l'equation recue.

    motif_2 = r"^(X\^([0-9])([0-9]*)|X)?$" 
    for i, element in enumerate(chaine):
        if element == 'X^0' or element == 'X^1' or element == 'X':
            if i + 1 != len(chaine) and chaine[i+ 1] not in '+-':
                print("Please enter a valid equation !")
                exit()
        if 'X' in element and re.match(motif_2, element) is None:
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
    