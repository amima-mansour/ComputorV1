# coding: utf-8

import mathematics as math

class Equation:
    """ C'est la classe Equation : 
    - a : le coeficient de x puissance 2
    - b : le coeficient de x puissance 1
    - c : le coeficient de x puissance 0
    - d : le degree de l'equation
    - str_equation : la forme reduite de l'equation."""

    def __init__(self, chaine):
        """ Le constructeur de la classe Equation."""

        self.str_equation, self.d, self.coeff = math.reduced_form(chaine)

    def form(self):
        """ Méthode qui affiche la forme reduite de l'equation."""

        print("Reduced form: {}".format(self.str_equation))

    def degree(self):
        """ Méthode qui affiche le degrée de l'equation."""
        
        if self.d == -1:
            print("Polynomial degree: 0")
        else:
            print("Polynomial degree: {}".format(self.d))

    def solutions(self):
        """ Méthode qui affiche les solution de l'equation."""

        if self.d == 0:
            print("The solution is:\nAll real numbers")
        elif self.d == -1:
            print("The solution is:\nImpossible")
        elif self.d > 2:
            print("The polynomial degree is stricly greater than 2, I can't solve.")
        else:
            c = 0
            b = 0
            if 'X^0' in self.coeff.keys():
                c = self.coeff['X^0']
            if 'X^1' in self.coeff.keys(): 
                b = self.coeff['X^1']
            if self.d == 1:
                solution = -1 * c / b
                if type(solution) == float:
                    solution = round(solution, 6)
                print("The solution is:\n{}".format(solution))
            else:
                a = self.coeff['X^2']
                math.solutions(a, b, c)