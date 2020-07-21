#coding utf-8
import time

def main(n):
    """ Boucle de recherche et calcul de la somme des n premiers nombres premiers
    Entrée : valeur maximum du plus grand nombre premier
    Sortie : écran
    """
    print(f'La somme des nombres premiers inférieurs à {n} est ', end='')

    premiers = list()
    premiers = PremierSuivant(premiers)
    # i = 0
    while premiers[-1] < n:
        premiers = PremierSuivant(premiers)
    premiers.pop(-1)

    somme = 0
    for i, v in enumerate(premiers):
        somme += int(v)
        # print (v, somme)
    print(f'{somme}')
    # print(f'premiers={premiers}')

def PremierSuivant(lp):
    """ Recherche du nombre premier suivant
    Entrée : liste des nombres premiers trouvés
    Sortie : liste des nombres premiers mise à jour avec le premier suivant
    """
    # print(f'lp={lp} ')
    if len(lp) == 0:
        compteur = 2
        lp.append(compteur)
    else:
        compteur = lp[-1]+1
        indexlp = 0
        trouvé = False
        while not trouvé and indexlp < len(lp):
            if compteur%lp[indexlp] == 0:
                compteur += 1
                indexlp = 0
            else:
                if indexlp == len(lp)-1:
                    lp.append(compteur)
                    trouvé = True
                else:
                    indexlp +=1
    return lp

if __name__ == "__main__":
    start_time = time.time()
    main(10)
    print(f'Durée d\'exécution : {time.time()-start_time}s.')
    start_time = time.time()
    main(200_000)
    print(f'Durée d\'exécution : {time.time()-start_time}s.')
    # start_time = time.time()
    # main(2_000_000)
    # print(f'Durée d\'exécution : {time.time()-start_time}s.')
