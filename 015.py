#coding utf-8

import time
import itertools

class Permutations():
    def __init__(self):
        self.n = int()
        self.r = list()

    def factoriel(self, n):
        x = 1
        for i in range(2, n+1):
            x *= i
        return x

    def Calculer(self, n, r=[]):
        self.n = n
        self.r = r

        x = self.factoriel(n)
        for m in r:
            y = self.factoriel(m)
            x //= y
        return x
    
    def Afficher(self, lst, rep=True):
        """Retourne la liste de toutes les permutations de lst (non récursif)
        si rep=False : suppression des répétitions de lst
        """
        # print(lst)
        permut = [lst]
        taille = len(lst)-1
        for verrou in range(taille):
            # print(f'verrou={verrou}: ')
            for i in range(len(permut)):
                z = permut[i][:]
                # print(f'\tz={z}, ', end='')
                for c in range(taille-verrou):
                    z.append(z.pop(verrou))
                    # print(f'puis z={z}', end='')
                    if rep == True or (z not in permut):
                        permut.append(z[:])
                    # if c < taille-verrou:
                    #     print(', ', end='')
                # print()
        return permut

if __name__ == '__main__':
    for n in [4, 6, 8, 10, 12, 14]:
        starttime = time.time()
        r = [n//2, n//2]
        p = Permutations()
        print(f'Une permutation de {n} items permet {p.Calculer(n)} possibilités.')
        print(f'Une permutation de {n} items sans répétition de {r} permet {p.Calculer(n, r)} possibilités.')
        perm = p.Afficher(list(itertools.repeat('\u2192', n//2)) + list(itertools.repeat('\u2193', n//2)), rep = False)
        c = 1
        for i in sorted(perm):
            print(f'{c}.{i}')
            c += 1
        print(f'Durée d\'exécution : {time.time()-starttime}s.')
    starttime = time.time()
    n = 40
    r = [n//2, n//2]
    print(f'Une permutation de {n} items sans répétition de {r} permet {p.Calculer(n, r)} possibilités.')
    print(f'Durée d\'exécution : {time.time()-starttime}s.')
