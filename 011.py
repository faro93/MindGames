# coding utf-8
""" Classes pour effectuer des opérations sur une matrice
Class Matrice
    Entrée : liste contenant la matrice (LxC)
    Méthodes :
        __init__ : initialisation de la matrice avec NUMPY
    hListe, vListe, dListe : retourne la liste des valeurs souhaitées
"""
import time
import numpy as np

matriceList = [[8, 2, 22, 97, 38, 15, 0, 40, 0, 75, 4, 5, 7, 78, 52, 12, 50, 77, 91, 8],
               [49, 49, 99, 40, 17, 81, 18, 57, 60, 87, 17, 40, 98, 43, 69, 48, 4, 56, 62, 00],
               [81, 49, 31, 73, 55, 79, 14, 29, 93, 71, 40, 67, 53, 88, 30, 3, 49, 13, 36, 65],
               [52, 70, 95, 23, 4, 60, 11, 42, 69, 24, 68, 56, 1, 32, 56, 71, 37, 2, 36, 91],
               [22, 31, 16, 71, 51, 67, 63, 89, 41, 92, 36, 54, 22, 40, 40, 28, 66, 33, 13, 80],
               [24, 47, 32, 60, 99, 3, 45, 2, 44, 75, 33, 53, 78, 36, 84, 20, 35, 17, 12, 50],
               [32, 98, 81, 28, 64, 23, 67, 10, 26, 38, 40, 67, 59, 54, 70, 66, 18, 38, 64, 70],
               [67, 26, 20, 68, 2, 62, 12, 20, 95, 63, 94, 39, 63, 8, 40, 91, 66, 49, 94, 21],
               [24, 55, 58, 5, 66, 73, 99, 26, 97, 17, 78, 78, 96, 83, 14, 88, 34, 89, 63, 72],
               [21, 36, 23, 9, 75, 00, 76, 44, 20, 45, 35, 14, 00, 61, 33, 97, 34, 31, 33, 95],
               [78, 17, 53, 28, 22, 75, 31, 67, 15, 94, 3, 80, 4, 62, 16, 14, 9, 53, 56, 92],
               [16, 39, 5, 42, 96, 35, 31, 47, 55, 58, 88, 24, 00, 17, 54, 24, 36, 29, 85, 57],
               [86, 56, 00, 48, 35, 71, 89, 7, 5, 44, 44, 37, 44, 60, 21, 58, 51, 54, 17, 58],
               [19, 80, 81, 68, 5, 94, 47, 69, 28, 73, 92, 13, 86, 52, 17, 77, 4, 89, 55, 40],
               [4, 52, 8, 83, 97, 35, 99, 16, 7, 97, 57, 32, 16, 26, 26, 79, 33, 27, 98, 66],
               [88, 36, 68, 87, 57, 62, 20, 72, 3, 46, 33, 67, 46, 55, 12, 32, 63, 93, 53, 69],
               [4, 42, 16, 73, 38, 25, 39, 11, 24, 94, 72, 18, 8, 46, 29, 32, 40, 62, 76, 36],
               [20, 69, 36, 41, 72, 30, 23, 88, 34, 62, 99, 69, 82, 67, 59, 85, 74, 4, 36, 16],
               [20, 73, 35, 29, 78, 31, 90, 1, 74, 31, 49, 71, 48, 86, 81, 16, 23, 57, 5, 54],
               [1, 70, 54, 71, 83, 51, 54, 69, 16, 92, 33, 48, 61, 43, 52, 1, 89, 19, 67, 48]]
class Matrice():
    """ Calcul du plus gd produit de n nombres dans la matrice
    Entrée : nombres de facteurs
    Sortie : écran
    """
    def __init__(self, matrice):
        self.matrice = np.array(matrice)

    def info(self, hauteur=False, largeur=False):
        """ Affiche les informations de la matrice
        """
        if largeur:
            return self.matrice.shape[0]
        if hauteur:
            return self.matrice.shape[1]
        print(f'matrice :\n{self.matrice}')
        print(f'\tdimension : {self.matrice.ndim}')
        print(f'\tforme : {self.matrice.shape}')
        print(f'\ttype : {self.matrice.dtype} ({self.matrice.itemsize} octets)')
        print('\ttaille :',\
            f'{self.matrice.shape[0]*self.matrice.shape[1]*self.matrice.itemsize} octets')

    def hListe(self, ligne, colonne, taille):
        """ hListe : retourne la liste de valeurs horizontales de gauche à droite à partir
        de l'index index et du nombre d'éléments taille
        Entrée : int(ligne, colonne, taille) : (ligne et colonne de départ, taille de la liste à considérer)
        Sortie : liste
        """
        liste = list()
        # print(f'ligne={ligne}, colonne={colonne}, taille={taille}')
        if colonne+(taille-1) < self.matrice.shape[1] and ligne < self.matrice.shape[0]:
            liste = self.matrice[ligne,colonne:(colonne+taille)]
        return liste

    def vListe(self, ligne, colonne, taille):
        """ vListe : retourne la liste de valeurs verticales de haut en bas à partir
        de l'index index et du nombre d'éléments taille
        Entrée : int(ligne, colonne, taille) : (ligne et colonne de départ, taille de la liste à considérer)
        Sortie : liste
        """
        liste = list()
        # print(f'ligne={ligne}, colonne={colonne}, taille={taille}')
        if ligne+(taille-1) < self.matrice.shape[0]:
            liste = self.matrice[ligne:(ligne+taille), colonne]
        return liste


    def ddListe(self, ligne, colonne, taille):
        """ ddListe : retourne la liste de valeurs en diagonal de gauche à droite et de haut en bas à partir
        de l'index index et du nombre d'éléments taille
        Entrée : int(ligne, colonne, taille) : (ligne et colonne de départ, taille de la liste à considérer)
        Sortie : liste
        """
        liste = list()
        lliste = list()
        cliste = list()
        # print(f'ligne={ligne}, colonne={colonne}, taille={taille}')
        if ligne+(taille-1) < self.matrice.shape[0] and colonne+(taille-1) < self.matrice.shape[1]:
            for c in range(colonne, colonne+taille):
                cliste.append(c)
            for l in range(ligne, ligne+taille):
                lliste.append(l)
            # print(f'lliste={lliste}, cliste={cliste} ')
            liste = self.matrice[lliste, cliste]
        return liste

    def dgListe(self, ligne, colonne, taille):
        """ dgListe : retourne la liste de valeurs en diagonal de droite à gauche et de haut en bas à partir
        de l'index index et du nombre d'éléments taille
        Entrée : int(ligne, colonne, taille) : (ligne et colonne de départ, taille de la liste à considérer)
        Sortie : liste
        """
        liste = list()
        lliste = list()
        cliste = list()
        # print(f'ligne={ligne}, colonne={colonne}, taille={taille}')
        if ligne+(taille-1) < self.matrice.shape[0] and colonne-(taille-1) >= 0 and colonne < self.matrice.shape[1]:
            for c in range(colonne, colonne-taille, -1):
                cliste.append(c)
            for l in range(ligne, ligne+taille):
                lliste.append(l)
            # print(f'lliste={lliste}, cliste={cliste} ')
            liste = self.matrice[lliste, cliste]
        return liste

class Produit():
    def __new__(self, liste):
        p = 1
        for f in liste:
            p *= f
        return p

class Compare():
    def __new__(self, t):
        pmax = {"p": 0, "l": 0, "c": 0, "liste": list()}
        for l in range(0, m.info(hauteur=True)):
            for c in range(0, m.info(largeur=True)):
                hliste = m.hListe(l, c, t)
                vliste = m.vListe(l, c, t)
                ddliste = m.ddListe(l, c, t)
                dgliste = m.dgListe(l, c, t)
                pliste = list()
                pliste.append(Produit(hliste))
                pliste.append(Produit(vliste))
                pliste.append(Produit(ddliste))
                pliste.append(Produit(dgliste))
                p = max(pliste)
                if pliste.index(p) == 0:
                    liste = hliste
                elif pliste.index(p) == 1:
                    liste = vliste
                elif pliste.index(p) == 2:
                    liste = ddliste
                elif pliste.index(p) == 3:
                    liste = dgliste
                if p > pmax.get("p"):
                    pmax = {"p": p, "l": l, "c": c, "liste": liste}
        print(f'Le plus grand produit {pmax.get("p")} est composé des facteurs {pmax.get("liste")} est situé en l{pmax.get("l")}c{pmax.get("c")}')

if __name__ == "__main__":
    start_time = time.time()
    m = Matrice(matriceList)
    m.info()
    Compare(4)
    print(f'Durée d\'exécution : {time.time()-start_time}s')
