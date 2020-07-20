#coding utf-8
import time

def main(somme):
    print(f'Recherche du triplet pythagoricien dont la somme est {somme}.')
    
    a = 1
    trouvé = False
    while a < somme and not trouvé:
        for b in range(1, somme+1, 1):
            cc = pow(a, 2) + pow(b,2)
            c = pow(cc, 0.5)
            if int(c) == c:
                if int(a+b+c) == somme:
                    trouvé = True
                    print(f'{a}²+{b}²={cc} -> c={int(c)}', end='')
                    print(f', a+b+c={int(a+b+c)}, a.b.c={int(a*b*c)}')
            if b == somme:
                a +=1


if __name__ == "__main__":
    start_time = time.time()
    main(12)
    print(f'Durée d\'exécution : {time.time()-start_time}s.')
    start_time = time.time()
    main(24)
    print(f'Durée d\'exécution : {time.time()-start_time}s.')
    start_time = time.time()
    main(1000)
    print(f'Durée d\'exécution : {time.time()-start_time}s.')