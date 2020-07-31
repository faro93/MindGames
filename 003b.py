#coding utf-8
import time

def main(n):
    print(f'Recherche du plus grand facteur premier pour {n}')
    premiers = list()
    facteurs = list()
    quotient = int()
    indexpremiers = 0
    divisé = n
    start_time = time.time()

    premiers = PremierSuivant(premiers)
    while quotient != 1:
        if divisé%premiers[indexpremiers] == 0:
            quotient = divisé//premiers[indexpremiers]
            divisé = quotient
            facteurs.append(premiers[indexpremiers])
        else:
            premiers = PremierSuivant(premiers)
            indexpremiers += 1

    # for n in range(1000):
    #     premiers = PremierSuivant(premiers)
    #     print(f'premiers={premiers} ')

    print(f'Le produit de facteurs premiers de {n} est : ',end='')
    for i in range(len(facteurs)):
        print(f'{facteurs[i]}', end='')
        if i != len(facteurs)-1:
            print(f'x', end='')
    print('')
    print(f'Le plus grand facteur premier de {n} est {facteurs[-1]}')
    print(f'Durée d\'exécution : {time.time()-start_time}s.')

def PremierSuivant(lp):
    # print(f'lp={lp} ')
    if len(lp) == 0:
        compteur = 2
        lp.append(compteur)
    else:
        compteur = lp[-1]+1
        indexlp = 0
        trouvé = False
        while trouvé == False and indexlp < len(lp):
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
    # main(12)
    # print()
    # main(28)
    # print()
    for i in (3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210, 231, 253, 276, 300, 325, 351, 378, 406, 435):
        main(i)
        print('#######################')
    # main(154)
    # main(13195)
    # print()
    # main(600851475143)
