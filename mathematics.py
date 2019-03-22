# coding: utf-8

def convertir_en_nombre(chaine):
    # Cette fonction convertit une en un nombre.

    if '.' in chaine:
        return float(chaine)
    else:
        return int(chaine)

def identifier_coefficients(liste):
    # Cette fonction identifie les differents coefficients de l'equation.

    a = 0 # coefficient de x a la puissance 2
    b = 0 # coefficient de x a la puissance 1
    c = 0 # coefficient de x a la puissance 0
    for i, element in enumerate(liste):
        if element ==  'X^0':
            coeff = 1
            if i - 3 >= 0 and liste[i - 3] == '-':
                coeff = -1
            c = c + coeff * convertir_en_nombre(liste[i - 2])
        elif element ==  'X^1':
            coeff = 1
            if i - 3 >= 0 and liste[i - 3] == '-':
                coeff = -1
            b = b + coeff * convertir_en_nombre(liste[i - 2])
        elif element ==  'X^2':
            coeff = 1
            if i - 3 >= 0 and liste[i - 3] == '-':
                coeff = -1
            a = a + coeff * convertir_en_nombre(liste[i - 2])
        else:
            continue
    return a, b, c

def reduced_string(a, b, c):
    # Cette fonction determine la forme reduite de l'equation sous forme de chaine de caractere.

    chaine = str()
    if c != 0:
        chaine += str(c) + " * X^0 "
    if b != 0:
        if b > 0:
            chaine += "+ " + str(b) + " * X^1 "
        else:
            d = b * -1
            chaine += "- " + str(d) + " * X^1 "
    if a != 0:
        if a > 0:
            chaine += "+ " + str(a) + " * X^2 "
        else:
            e = a * -1
            chaine += "- " + str(e) + " * X^2 "
    chaine += "= 0"
    return chaine 


def reduced_form(chaine):
    # Cette fonction determine la forme reduite de l'equation.
    
    equality = chaine.split('=')
    left = equality[0].split()
    right = equality[1].split()
    a, b, c = identifier_coefficients(left)
    d, e, f = identifier_coefficients(right)
    a -= d
    b -= e
    c -= f
    chaine = reduced_string(a, b, c)
    if a:
        degree = 2
    elif b:
        degree = 1
    else:
        degree = 0
    if degree == 0:
        chaine = "x = x"
    return chaine, degree, a, b, c

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
        print ("Discriminant is null, the solution is:\n{}".format(-1 * b / (2 * a)))
    elif discriminant > 0:
        racine = racine_carre(discriminant)
        print(racine)
        solution_1 = (-1 * b + racine) / (2  * a)
        solution_2 = (-1 * b - racine) / (2  * a)
        print("Discriminant is strictly positive, the two solutions are:\n{}\n{}".format(solution_1, solution_2))
    else:
        racine = racine_carre(-1 * discriminant)
        premiere_partie = -1 * b / (2 * a)
        seconde_partie =  racine / (2  * a)
        print("Discriminant is strictly negative, the two solutions are:\n{} + i * {}\n{} - i * {}".format(premiere_partie,
            seconde_partie, premiere_partie, seconde_partie))