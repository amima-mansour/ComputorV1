# coding: utf-8

import re

def convertir_en_nombre(chaine):
    # Cette fonction convertit une en un nombre.

    if '.' in chaine:
        return float(chaine)
    else:
        return int(chaine)

def identifier_coefficients(liste):
    # Cette fonction identifie les differents coefficients de l'equation.

    coeff = {}
    for i, element in enumerate(liste):
        if 'X' in element:
            b = 1
            if i - 3 >= 0 and liste[i - 3] == '-':
                b = -1
            if element == 'X':
                element = 'X^1'
            if element in coeff.keys():
                coeff[element] += b * convertir_en_nombre(liste[i - 2])   
            else:
                coeff[element] = b * convertir_en_nombre(liste[i - 2])
        elif re.match(r"(-)?[0-9]+(\.[0-9]+)?", element):
            if i + 1 == len(liste) or liste[i + 1] != '*':
                b = 1
                if i - 1 >= 0 and liste[i - 1] == '-':
                    b = -1
                if 'X^0' in coeff.keys():
                    coeff['X^0'] += b * convertir_en_nombre(liste[i])   
                else:
                    coeff['X^0'] = b * convertir_en_nombre(liste[i])
        else:
            continue
    return coeff

def reduced_string(coeff_final):
    # Cette fonction determine la forme reduite de l'equation sous forme de chaine de caractere.

    chaine = str()
    i = 0
    if len(coeff_final) == 1 and "X^0" in coeff_final:
        if coeff_final["X^0"] == 0:
            return 0, "X = X"
        else:
            return  -1, str(coeff_final["X^0"])+ " = 0"
    while len(coeff_final) > 0:
        degree = "X^"+ str(i)
        #while degree not in coeff_final.keys():
        #    i += 1
        #    degree = "X^"+ str(i)
        if degree not in coeff_final.keys():
            coeff_final[degree] = 0
        if coeff_final[degree] >= 0:
            chaine += " + " + str(coeff_final[degree]) + " * "+ degree
        else:
            d = -1 * coeff_final[degree]
            chaine += " - " + str(d) + " * "+ degree
        del coeff_final[degree]
        i += 1
    chaine += " = 0"
    return i - 1, chaine 


def reduced_form(chaine):
    # Cette fonction determine la forme reduite de l'equation.
    
    equality = chaine.split('=')
    left = equality[0].split()
    right = equality[1].split()
    coeff_gauche = identifier_coefficients(left)
    coeff_droite = identifier_coefficients(right)
    coeff_final = {}
    for element in coeff_gauche:
        if element in coeff_droite.keys():
            coeff_final[element] = coeff_gauche[element] - coeff_droite[element]
            coeff_droite[element] = 0
        else:
            coeff_final[element] = coeff_gauche[element]
    for element in coeff_droite:
        if coeff_droite[element]:
            coeff_final[element] = -1 * coeff_droite[element]
    coeff_final_copy = coeff_final.copy()
    degree, chaine = reduced_string(coeff_final_copy)
    if degree > 0:
        chaine = chaine[3:]
    return chaine, degree, coeff_final

def racine_carre(nombre):
    # Cette fonction calcule la racine carree d'un nombre 

    i = 0.000001
    while i * i < nombre:
        resultat = i 
        i += 0.000001
    return resultat

def solutions(a, b, c):
    # Cette fonction trouve les solutions d'une equation de second degree.

    discriminant = b * b - 4 * a * c
    if discriminant == 0:
        solution = -1 * b / (2 * a)
        if type(solution) == float:
            solution = round(solution, 6)
        print ("Discriminant is null, the solution is:\n{}".format(solution))
    elif discriminant > 0:
        racine = racine_carre(discriminant)
        solution_1 = (-1 * b + racine) / (2  * a)
        solution_2 = (-1 * b - racine) / (2  * a)
        if type(solution_1) == float:
            solution_1 = round(solution_1, 6)
        if type(solution_2) == float:
            solution_2 = round(solution_2, 6)
        print("Discriminant is strictly positive, the two solutions are:\n{}\n{}".format(solution_2, solution_1))
    else:
        racine = racine_carre(-1 * discriminant)
        premiere_partie = -1 * b / (2 * a)
        seconde_partie =  racine / (2  * a)
        if type(premiere_partie) == float:
            premiere_partie = round(premiere_partie, 6)
        if type(seconde_partie) == float:
            seconde_partie = round(seconde_partie, 6)
        print("Discriminant is strictly negative, the two solutions are:\n{} - i * {}\n{} + i * {}".format(premiere_partie,
            seconde_partie, premiere_partie, seconde_partie))