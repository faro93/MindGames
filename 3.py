# coding utf-8
import time

class enigme3():
    def __init__(self,nb):
        self.diviseurs = list()
        self.diviseurs.append(nb)

        self.FindAllFactors(nb)
        
        self.diviseurs = sorted(self.diviseurs)
        self.diviseurs = self.RemoveComposedFactors(self.diviseurs, nb)

        print(f'Les diviseurs premiers de {nb} sont {self.diviseurs[1:-1]} ')
        print(f'Le plus grand diviseur premier de {nb} est {self.diviseurs[-2]}')
    
    def FindAllFactors(self, n):
        compteur = n-1
        i=0

        print(f'Recherche des diviseurs de {n} ') #, end='')
        while compteur > 0:
            reste = n%compteur
            if reste == 0:
                # print(f'0.{n}%{compteur}={reste}')
                if not compteur%2 == 0:
                    # print(f'1.{compteur}%2={compteur%2}')
                    self.diviseurs.append(compteur)
                else:
                    if not 2 in self.diviseurs:
                        self.diviseurs.append(2)
            compteur -= 1
            i += 1
            if i%100_000_000 == 0:
                print(f'compteur={compteur}, diviseurs={self.diviseurs}',
                      end='\r', flush=True)
        print(f' : ok')
    
    def RemoveComposedFactors(self, l, n):
        div = l[1:-1]
        rdiv = sorted(div, reverse=True)
        m = list()

        # print(div)
        # print(rdiv)
        
        print(f'Suppression des diviseurs composés de {n} ', end='')
        for r in rdiv:
            stopdiv = False
            dindex = 0
            while stopdiv == False and dindex < len(div):
                # print(f'r={r}, d={div[dindex]}, mod={r%div[dindex]} ')
                if r%div[dindex] == 0 and r != div[dindex]:
                    m.append(r)
                    # print(f'm={m}')
                    stopdiv = True
                else:
                    dindex += 1
        # print(f'm={m}')

        for n in m:
            l.remove(n)
        print(f' : ok')
        return l


if __name__ == "__main__":
    # start_time = time.time()
    # enigme3(24)
    # print(f'Exécution en {time.time()-start_time}s\n')
    # start_time = time.time()
    # enigme3(13195)
    # print(f'Exécution en {time.time()-start_time}s\n')
    start_time = time.time()
    enigme3(600851475143)
    print(f'Exécution en {time.time()-start_time}s\n')