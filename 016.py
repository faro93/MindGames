# coding utf-8
import time

def main(n, p):
    r = 1
    for i in range(p):
        r *= n

    s = 0
    for i in str(r):
        s += int(i)
    
    print(f'La somme des chiffres de {n} à la puissance {p} est {s}.')
if __name__ == '__main__':
    starttime = time.time()
    main(2, 1000)
    print(f'Duréee d\'exécution : {time.time()-starttime} ')