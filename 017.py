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
        self.Ecrire(self.chiffres)

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
                chaine.insert(0, self.tens[liste[i]-1])
            elif i == 2:
                if liste[0] != 0 or liste[1] != 0:
                    chaine.insert(0, 'and')
                if liste[i] != 0:
                    chaine.insert(0, self.unities[liste[i]] + ' ' + self.hundred[0])
            elif i == 3:
                if i < len(liste)-1 and liste[i]+liste[i+1]*10 < 20 and not thousands:
                    if liste[i] != 0 or liste[i+1] == 1:
                        chaine.insert(0, self.unities[liste[i]+liste[i+1]*10] + ' ' + self.thousand[0] + ' and ')
                        thousands = True
                elif not thousands:
                    if liste[2] != 0:
                        chaine.insert(0, 'and')
                    chaine.insert(0, self.unities[liste[i]] + ' ' + self.thousand[0])
            # if i == 3 and not thousands:
            #     if liste[2] != 0:
            #         chaine.insert(0, 'and')
            #     chaine.insert(0, self.unities[liste[i]] + ' ' + self.thousand[0])
            elif i > 3 and not thousands:
                chaine.insert(0, self.tens[liste[i]])
        # print(f'{chaine}')
        for i in range(len(chaine)):
            print(chaine[i] + ' ', end='')
        print()


if __name__ == '__main__':
    starttime = time.time()
    # main(1000)
    n = Nombre()

    x = 19111
    print(f'{x} : ', end='')
    n.Décomposer(x)

    x = 20364
    print(f'{x} : ', end='')
    n.Décomposer(x)

    # for x in (0, 10, 100, 1000, 12345, 999):
    #     print(f'{x} : ', end='')
    #     n.Décomposer(x)

    for x in range(140, 180):
        print(f'{x} : ', end='')
        n.Décomposer(x)
    print(f'Durée d\'exécution : {time.time()-starttime}s.')