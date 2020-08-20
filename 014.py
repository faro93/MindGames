# coding utf-8
import time

def main(n):
    maxi = [0, 0, []]
    while n > 1:
        r = séquence(n)
        c = r[0]
        if c > maxi[1]:
            maxi[0] = n
            maxi[1] = c
            maxi[2] = r[1]
        n -= 1
    print(f'La longueur de la séquence pour la valeur {maxi[0]} est {maxi[1]}.')
    c = maxi[1]
    for i in maxi[2]:
        print(f'{i}', end='')
        c -= 1
        if c > 0:
            print(' -> ', end='')    
    print()

def séquence(n):
    res = n
    c = 1
    l = list()
    l.append(n)
    while res > 1:
        if res%2 == 0:
            res = paire(res)
        else:
            res = impaire(res)
        # print(res)
        l.append(res)
        c += 1
    return (c, l)

def paire(n):
    return n//2

def impaire(n):
    return (3*n+1)

if __name__ == "__main__":
    starttime = time.time()
    main(1_000_000)
    print(f'Duréee d\exécution : {time.time()-starttime}s.')