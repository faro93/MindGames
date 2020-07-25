# coding utf-8
import time

def main(n):
    i = 1
    s = 0
    print(f'La somme des nombres premiers inférieurs à {n} est ', end='')
    while i < n:
        i += 1
        if premier(i):
            s += i
    print(s)

def premier(n):
    if n%2 == 0:
        return n == 2
    d = 3

    while pow(d,2) <= n:
        if n%d == 0:
            return 0
        d += 2
    return 1

if __name__ == "__main__":
    start_time = time.time()
    main(10)
    print(f'Durée d\'exécution : {time.time()-start_time}s')
    start_time = time.time()
    main(200_000)
    print(f'Durée d\'exécution : {time.time()-start_time}s')
    start_time = time.time()
    main(2_000_000)
    print(f'Durée d\'exécution : {time.time()-start_time}s.')
