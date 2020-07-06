# coding utf-8

import time

class Ediv():
    def __init__(self, max):
        self.max = max

    def Recherche(self):
        pass

if __name__ == "__maine__":
    start_time = time.time()
    i = Ediv(20)
    print(f'Exécution en {time.time()-start_time}s.')