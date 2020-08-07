# coding utf-8
"""Factorise en nombres premiers avec une liste externe de manière
optimisée
But :   utiliser une liste, mais ne pas la remplir à chaque nouvelle
        valeur/factorisation qd ce n'est pas nécessaire.
"""

import time

def main(n):
    Factorise(n)

def Factorise(n):
    nb = 2
    if premiers == []:
        premiers.append(nb)

    indexpremiers = 0
    divisé = n
    quotient = int()
    facteurs = list()
    while quotient != 1:
        if divisé%premiers[indexpremiers] == 0:
            quotient = divisé//premiers[indexpremiers]
            divisé = quotient
            facteurs.append(premiers[indexpremiers])
        else:
            if indexpremiers < len(premiers)-1:
                indexpremiers += 1
            else:
                nb += 1
                while not Premier(nb):
                    nb += 1
                premiers.append(nb)
                indexpremiers += 1
    print(f'facteurs {facteurs}')
    return facteurs


def Premier(n):
    if n%2 == 0:
        return n == 2
    d = 3
    while pow(d,2) <= n:
        if n%d == 0:
            return 0
        d += 2
    return 1

if __name__ == "__main__":
    starttime = time.time()
    premiers = list()
    main(76)
    print(f'Liste des nombres premiers :\n{premiers}')
    main(21)
    print(f'Liste des nombres premiers :\n{premiers}')
    print(f'Durée d\'exécution : {time.time()-starttime}s.')