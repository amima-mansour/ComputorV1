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

        self.str_equation, self.d, self.a, self.b, self.c = math.reduced_form(chaine)

    def form(self):
        """ Méthode qui affiche la forme reduite de l'equation."""

        print("Reduced form: {}".format(self.str_equation))

    def degree(self):
        """ Méthode qui affiche le degrée de l'equation."""

        print("Polynomial degree: {}".format(self.d))

    def solutions(self):
        """ Méthode qui affiche les solution de l'equation."""

        if self.d == 0:
            print("The solution is:\nAll real numbers")
        else:
            if self.d == 1:
                solution = -1 * self.c / self.b 
                print("The solution is:\n{}".format(solution))
            else:
                math.solutions(self.a, self.b, self.c)







    




