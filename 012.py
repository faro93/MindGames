# coding utf-8
import time

class Triangle():
    def __init__(self):
        compteur = 0
        somme = 0
        triangle = list()
        trouvé = False
        while not trouvé:
            compteur += 1
            triangle.append(compteur)
            s = str()
            print(f'Triangle{compteur}: ', end='')
            somme += compteur
            t = len(triangle)
            for i in range(t):
                s += str(triangle[i])
                if i < t-1:
                    s += '+'
            print(f'{somme}={s}')
            if compteur == 29:
                trouvé = True

class Diviseurs():
    def __new__(self, taille):
        self.taille = taille


if __name__ == "__main__":
    start_time = time.time()
    Triangle()
    print(f'Durée d\'exécution : {time.time()-start_time}s.')