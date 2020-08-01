# coding utf-8
import time

class Triangle():
    """
    Retourne la somme des entiers naturels de 1 à n
    """
    def __new__(self, n):
        somme = 0
        triangle = list()
        for i in range(1, n+1):
            somme += i
            triangle.append(i)
        return somme

class Factoriel():
    """
    Retourne n!
    """
    def __new__(self, n):
        # print(f'Factoriel({n})=', end='')
        p = 1
        for i in range(1, n+1):
            p *= i
        # print(p)
        return p

class Diviseurs():
    """
    Classe de dénombrement de diviseurs\n
    Méthodes :\n
    \tCompte(list facteurs) = int compte
    \tDénombre(list facteurs) = list diviseurs
    """
    def __init__(self):
        self.diviseurs = list()
        self.combinaisons = list()
        self.compte = int()

    def Compte(self, facteurs):
        """ Compte les combinaisons possibles pour n nombres\n
        nombre de combinaisons de k parmi n : n!/(k!(n-k)!)
        """
        n = len(facteurs)
        s = 0
        for k in range(1, n+1):
            s += int(Factoriel(n)/(Factoriel(k)*Factoriel(n-k)))
            self.compte = s+1 # ajout du diviseur 1 (neutre)
        return self.compte

    def Dénombre(self, facteurs):
        """ Dénombre les diviseurs d'après la liste des facteurs
        """
        nf = len(facteurs)
        for nf in range(1, len(facteurs)+1):
            print(f'Nombre de facteurs : {nf}')
                

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
        self.premiers = list()
        self.facteurs = list()
        self.quotient = int()
        self.indexpremiers = 0
        self.nombre = 2

        # self.facteurs.append(1)

    def Factorise(self, n):
        """
        Factorise n par des nombres premiers et génère une liste de ces facteurs
        """
        self.divisé = n
        if Premier(self.nombre):
            self.premiers.append(self.nombre)
        while self.quotient != 1:
            if self.divisé%self.premiers[self.indexpremiers] == 0:
                self.quotient = self.divisé//self.premiers[self.indexpremiers]
                self.divisé = self.quotient
                self.facteurs.append(self.premiers[self.indexpremiers])
            else:
                self.nombre += 1
                while not Premier(self.nombre):
                    self.nombre += 1
                self.premiers.append(self.nombre)
                self.indexpremiers += 1
        return self.facteurs

    def Affiche(self, n, facteurs):
        """
        Affiche la produits des nombres premiers
        """
        print(f'Le produit de facteurs premiers de {n} est : ',end='')
        for i in range(len(facteurs)):
            print(f'{facteurs[i]}', end='')
            if i != len(facteurs)-1:
                print(f'x', end='')
        print('')

if __name__ == "__main__":
    for n in (2, 3, 5, 7, 15):
        start_time = time.time()
        somme = Triangle(n)
        print(f'La somme du triangle naturel n°{n} est {somme}')
        f = Factorisation()
        facteurs = f.Factorise(somme)
        f.Affiche(somme, facteurs)
        d = Diviseurs()
        print(f'{somme} est divisible par {d.Compte(facteurs)} combinaisons')
        d.Dénombre(facteurs)
        print(f'Durée d\'exécution : {time.time()-start_time}s.\n')
