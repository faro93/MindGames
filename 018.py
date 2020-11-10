# coding utf-8
import time
import numpy as np

"""
By starting at the top of the triangle below and moving to
adjacent numbers on the row below, the maximum total from
top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

NOTE: As there are only 16384 routes, it is possible to solve
this problem by trying every route. However, Problem 67, is the
same challenge with a triangle containing one-hundred rows; it
cannot be solved by brute force, and requires a clever method! ;o)
"""
t1=[[3],
    [7, 4],
    [2, 4, 6],
    [8, 5, 9, 3]]

class Dijkstra():
    def __init__(self, m):
        self.m = m
        self.d = list()
        self.p = list()
        self.f = list()


    def info(self):
        """ Affiche les informations de la matrice
        """
        print(f'matrice :\n{self.m}')
        print(f'\tdimension : {self.m.ndim}')
        print(f'\tforme : {self.m.shape}')
        print(f'\ttype : {self.m.dtype} ({self.m.itemsize} octets)')
        print('\ttaille :',\
            f'{self.m.shape[0]*self.m.shape[1]*self.m.itemsize} octets')
        
    def PoidsLéger(self, r):
        self.InitPL(r)
        print(f'Recherche du plus court chemin à partir du sommet r={r}')
        self.Listes()
        while self.f:
            print(f'self.f={self.f}')

            self.f.pop(r)
        print(f'self.f={self.f}')


    def Init(self, r):
        self.d = [float('inf')]*self.m.shape[0]
        self.p = [None]*self.m.shape[0]
        self.f = [x for x in range(self.m.shape[0])]
        self.Listes()
        self.d[r] = 0

    def SommetSuivant(self, u):
        pass

    def Relachement(self, u , v):
        if self.d[v] > self.d[u]+

    def Listes(self):
        print(f'self.d={self.d}')
        print(f'self.p={self.p}')
        print(f'self.f={self.f}')
        print()

    def PoidsLourd(self):
        pass

class GraphicConvert():
    def __init__(self):
        pass

    def Triangle2Matrix(self, triangle):
        s = int()
        for i in triangle:
            s += len(i)

        m = np.zeros((s+1, s+1), np.int8)

        line = 0
        row = 1
        for i in range(len(triangle)):
            # print(f'triangle[{i}]={triangle[i]}')
            if len(triangle[i]) < 2:
                # print(f'({line}, {row}) : {triangle[i][0]}')
                m.itemset((line, row), triangle[i][0])
            else:
                j = int()
                while j < len(triangle[i])-1:
                    line += 1
                    # print(f'({line}, {row}) : {triangle[i][j:j+2]}')
                    m.itemset((line, row), triangle[i][j])
                    m.itemset((line, row+1), triangle[i][j+1])
                    j += 1
                    row += 1
            row += 1

        return m

if __name__ == '__main__':
    starttime = time.time()
    print(f'triangle:')
    for l in t1:
            print(f'{l}')
    gc = GraphicConvert()
    m = gc.Triangle2Matrix(t1)
    # print(m)
    d = Dijkstra(m)
    d.info()
    d.PoidsLéger(0)
    print(f'Durée d\'exécution : {time.time()-starttime}s')