# coding utf-8

import time

class Ediv():
    def __init__(self, mdiv):
        self.mdiv = mdiv
        print(f'Recherche du plus petit entier  divisible sans reste par les valeurs de {self.mdiv} à 1.')

    def Recherche(self):
        trouvé = False
        compteur = self.mdiv
        div = self.mdiv
        while not trouvé and div != 0:
            # print(f'compteur={compteur}, div={div}, mod={compteur%div}')
            if compteur%div == 0:
                div -= 1
                if div == 0:
                    trouvé = True
                    print(f'Résultat={compteur}')
            else:
                div = self.mdiv
                compteur += self.mdiv
        return True

if __name__ == "__main__":
    start_time = time.time()
    i = Ediv(10)
    r = i.Recherche()
    print(f'Exécution en {time.time()-start_time}s.')
    start_time = time.time()
    i = Ediv(20)
    r = i.Recherche()
    print(f'Exécution en {time.time()-start_time}s.')