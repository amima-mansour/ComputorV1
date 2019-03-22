# coding: utf-8

import sys
import equation
import test

if __name__ == "__main__":
    if len(sys.argv) == 1 or len(sys.argv) > 2:
        print("Please enter an equation !")
        exit()
    chaine = sys.argv[1]
    chaine = chaine.split("=")
    if len(chaine) == 1:
        print("Please enter a valid equation 6!")
        exit()
    grand_degree = sys.argv[1].split("^")
    i = 0
    #while i < len(grand_degree):
    #    if 'X' in grand_degree[i]:
    #        i += 1
    #        d = int(grand_degree[i].split()[0])
    #        if d > 2:
    #            print("Polynomial degree: {}".format(d))
    #            print("The polynomial degree is stricly greater than 2, I can't solve.")
    #            exit()
    test.premier_test(chaine)
    test.second_test(chaine)

    eq = equation.Equation(sys.argv[1])
    eq.form()
    eq.degree()
    eq.solutions()