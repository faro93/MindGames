# coding utf-8

import time

class Palindromes():
    def __init__(self):
        self.lp = list()
        self.lf = list()
        self.slp = list()

    def Recherche(self, ndigit):
        print(f'Recherche des palindromes par un produit de 2 nombre à {ndigit} chiffres')
        p1 = int('9'*ndigit)
        p2 = int('9'*ndigit)
        lp = list()
        lf = list()
        trouvé = False
        
        while (not trouvé) and p1 > int('9'*(ndigit-1)):
            # print(f'1.p1={p1}, ', end='')
            while (not trouvé) and p2 > int('9'*(ndigit-1)):
                # print(f'p2={p2}, ', end='')
                if str(p1*p2) == str(p1*p2)[::-1]:
                    if (p1, p2) not in lf and (p2, p1) not in lf:
                        # print(f'Le palindrome {p1*p2} est le produit de {p1}x{p2}')
                        lf.append((p1, p2))
                        lp.append(p1*p2)
                    # trouvé = True
                p2 -= 1
            p1 -= 1
            p2 = int('9'*ndigit)
        self.slp = self.Tri(lp, lf)
        return (self.slp, lp, lf)
    
    def Tri(self, lp, lf):
        slp = list()
        for i in sorted(lp):
            if i not in slp:
                slp.append(i)
        # print(slp)
        return slp

    def Afficher(self, slp, lp, lf):
        for i in slp:
            print(f'Le palindrome {i} est le produit de ', end='')
            trouvé = False
            for p in range(len(lp)):
                if lp[p] == i:
                    if trouvé:
                        print(', ', end='')
                    print(f'{lf[p][0]}x{lf[p][1]}', end='')
                    trouvé = True
                if p == len(lp)-1:
                    print()




if __name__ == "__main__":
    start_time = time.time()
    p = Palindromes()
    (slp, lp, lf) = p.Recherche(2)
    # p.Afficher(slp, lp, lf)
    print(p.slp[-1])
    print(f'Exécution en {time.time()-start_time}s.')
    start_time = time.time()
    p = Palindromes()
    (slp, lp, lf) = p.Recherche(3)
    # p.Afficher(slp, lp, lf)
    print(p.slp[-1])
    print(f'Exécution en {time.time()-start_time}s.')
    start_time = time.time()
    p = Palindromes()
    (slp, lp, lf) = p.Recherche(4)
    # p.Afficher(slp, lp, lf)
    print(p.slp[-1])
    print(f'Exécution en {time.time()-start_time}s.')