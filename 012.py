# coding utf-8
import time
import itertools
from numpy import prod

class Triangle():
    """
    Retourne la somme des entiers naturels de 1 à n
    """
    def __new__(self, n):
        somme = 0
        triangle = list(range(1, n+1))
        somme = sum(triangle)
        return somme

class Factoriel():
    """
    Retourne n!
    """
    def __new__(self, n):
        return prod(range(1, n+1))

class Diviseurs():
    """
    Classe de dénombrement de diviseurs\n
    Méthodes :\n
    \tCompte(list facteurs) = int compte
    \tDénombre(list facteurs) = list diviseurs
    """
    def __init__(self):
        self.diviseurs = list()

    def Compte(self, facteurs):
        """ Compte les combinaisons possibles pour n nombres\n
        nombre de combinaisons de k parmi n : n!/(k!(n-k)!)
        """
        n = len(facteurs)
        s = 0
        for k in range(1, n+1):
            s += int(Factoriel(n)/(Factoriel(k)*Factoriel(n-k)))
        return s+1 # ajout du diviseur 1 (neutre)

    def Dénombre(self, facteurs):
        """ Dénombre les diviseurs d'après la liste des facteurs
        """
        nf = len(facteurs)
        diviseurs = [1]
        for nf in range(1, len(facteurs)+1):
            combs = itertools.combinations(facteurs, nf)
            for liste in combs:
                diviseurs.append(prod(liste))
        self.diviseurs = sorted(set(diviseurs))

    def Affiche(self, n):
        print(f'{n} a {len(self.diviseurs)} diviseurs : ', end='')
        for i in range(len(self.diviseurs)):
            print(self.diviseurs[i], end='')
            if i < len(self.diviseurs)-1:
                print(', ', end='')
        print()


class Premier():
    """
    Retourne True si le nombre passé est premier, sinon False
    """
    def __new__(self, n):
        if n%2 == 0:
            return n == 2
        d = 3
        while pow(d,2) <= n:
            if n%d == 0:
                return 0
            d += 2
        return 1

class Factorisation():
    """
    Classe de factorisation\n
    Méthodes :\n
    \tFactorise(int n) = list(facteurs premiers)
    \tAffiche(list facteurs)
    """
    def __init__(self):
        # self.premiers = p
        self.facteurs = list()
        self.quotient = int()
        self.indexpremiers = 0
        self.nombre = 2
        self.divisé = int()

        # self.facteurs.append(1)

    def Factorise(self, n):
        """
        Factorise n par des nombres premiers et génère une liste de ces facteurs
        """
        self.divisé = n
        if Premier(self.nombre):
            if self.nombre not in premiers:
                premiers.append(self.nombre)
        while self.quotient != 1:
            if self.divisé%premiers[self.indexpremiers] == 0:
                self.quotient = self.divisé//premiers[self.indexpremiers]
                self.divisé = self.quotient
                self.facteurs.append(premiers[self.indexpremiers])
            else:
                self.nombre += 1
                while not Premier(self.nombre):
                    self.nombre += 1
                if self.nombre not in premiers:
                    premiers.append(self.nombre)
                self.indexpremiers += 1
        return self.facteurs

    def Affiche(self, n, facteurs):
        """
        Affiche la produits des nombres premiers
        """
        print(f'La décomposition en produit de facteurs premiers de {n} est ',end='')
        for i in range(len(facteurs)):
            print(f'{facteurs[i]}', end='')
            if i != len(facteurs)-1:
                print(f'x', end='')
        print('')

if __name__ == "__main__":
    start_time = time.time()
    premiers = list()
    n = 2 #106272 #34911 # n° du triangle
    trouvé = False
    ndiviseurs = 6
    while not trouvé and n < 8:
        somme = Triangle(n)
        f = Factorisation()
        facteurs = f.Factorise(somme)
        # print(f'{facteurs}, {set(facteurs)} ')
        d = Diviseurs()
        combinaisons = d.Compte(facteurs)
        c2 = d.Compte(set(facteurs))
        print(f'{combinaisons}, {c2}, {facteurs} ')
        if  combinaisons >= ndiviseurs:
            d.Dénombre(facteurs)
            if len(d.diviseurs) == ndiviseurs:
                print(f'La somme du triangle naturel n°{n} est {somme}')
                f.Affiche(somme, facteurs)
                print(f'{somme} est divisible par {combinaisons} combinaisons')
                d.Affiche(somme)
                print(f'Il y a {len(premiers)} nombres premiers dans la liste :\n{premiers}')
                trouvé = True
        n += 1
        # if time.time()-start_time > 300:
        #     trouvé = True
        #     print(f'Triangle naturel n°{n} en cours dont la somme est {somme}')
        #     f.Affiche(somme, facteurs)
        #     print(f'{somme} est divisible par {combinaisons} combinaisons')
        #     d.Dénombre(facteurs)
        #     d.Affiche(somme)
        #     print(f'Il y a {len(premiers)} nombres premiers dans la liste')
        # # print()
    print(f'Durée d\'exécution : {time.time()-start_time}s.\n')

