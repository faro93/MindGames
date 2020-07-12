#coding utf-8
import time

def main(n):
    print(f'Recherche du {n}ème nombre premier : ', end='')
    premiers = list()

    for i in range(n):
        premiers = PremierSuivant(premiers)
    print(f'{premiers[-1]}')
    # print(f'premiers={premiers}')

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
    start_time = time.time()
    main(10001)
    print()
    print(f'Durée d\'exécution : {time.time()-start_time}s.')
