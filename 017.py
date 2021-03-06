# coding utf-8
import time

class Nombre():
    def __init__(self):
        self.chiffres = list()
        self.nombre = list()
        # self.unities = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
        # self.teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen',
        #         'seventeen', 'eighteen', 'nineteen']
        self.unities = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine',
                'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen',
                'seventeen', 'eighteen', 'nineteen']
        self.tens = ['ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
        self.hundred =['hundred']
        self.thousand = ['thousand']
        self.order = [self.thousand, self.hundred, self.tens, self.unities]

    def Décomposer(self, n):
        self.chiffres.clear()

        while n >= 10:
            y = n//10
            y *= 10
            self.chiffres.append(n-y)
            n = y//10
        self.chiffres.append(n)
        c = self.Ecrire(self.chiffres)
        return c

    def Ecrire(self, liste):
        chaine = list()
        # print(f'{liste}')
        unities = False
        thousands = False
        for i in range(len(liste)):
            if i == 0:
                if i < 2 and len(liste) >= 2 and liste[0]+liste[1]*10 < 20  and not unities:
                    if liste[0] != 0 or liste[1] == 1:
                        chaine.insert(0, self.unities[liste[0]+liste[1]*10])
                        unities = True
                elif not unities:
                    if i < len(liste)-1 and liste[i] != 0:
                        chaine.insert(0, self.unities[liste[i]])
                    elif len(liste) == 1:
                        chaine.insert(0, self.unities[liste[i]])
            elif i == 1 and not unities:
                if liste[i] != 0:
                    chaine.insert(0, self.tens[liste[i]-1])
            elif i == 2:
                if liste[0] != 0 or liste[1] != 0:
                    chaine.insert(0, 'and')
                if liste[i] != 0:
                    chaine.insert(0, self.hundred[0])
                    chaine.insert(0, self.unities[liste[i]])
            elif i == 3:
                if i < len(liste)-1 and liste[i]+liste[i+1]*10 < 20 and not thousands:
                    if liste[i] != 0 or liste[i+1] == 1:
                        chaine.insert(0, 'and')
                        chaine.insert(0, self.thousand[0])
                        chaine.insert(0, self.unities[liste[i]+liste[i+1]*10])
                        thousands = True
                elif not thousands:
                    if liste[2] != 0:
                        chaine.insert(0, 'and')
                    chaine.insert(0, self.thousand[0])
                    if liste[i] != 0:
                        chaine.insert(0, self.unities[liste[i]])
            elif i > 3 and not thousands:
                chaine.insert(0, self.tens[liste[i]-1])

        for i in range(len(chaine)):
            print(chaine[i] + ' ', end='')
        print()
        return chaine


if __name__ == '__main__':
    starttime = time.time()
    n = Nombre()

    ch = list()
    s = int()
    for x in range(1, 1001):
        print(f'{x} : ', end='')
        ch = n.Décomposer(x)
        for i in ch:
            s += len(i)
            print(f'\'{i}\' a {len(i)} caractères, la somme des caractères est {s}.')
    print(f'Durée d\'exécution : {time.time()-starttime}s.')