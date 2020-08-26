# coding utf-8
import time

def main(n):
    print(f'n={n} ')
    unities = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen',
             'seventeen', 'eighteen', 'nineteen']
    tens = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    hundred =['hundred']
    thousand = ['thousand']

    result = str()
    for i in range(100):
        print(f'i={i} : ', end='')
        if i < 10:
            print(f'{unities[i]}', end='')
        elif i < 20:
            print(f'{teens[i-10]}', end='')
        else:
            if i >= 100:
                print(f'{unities[i//100]} ', end='')
                print(f'{hundred[0]} and ', end='')
                i -= (i//100)*100
            if i%10 == 0 :
                print(f'{tens[i//10-2]}', end='')
            else:
                print(f'{tens[i//10-2]}-{unities[i-(i//10)*10]}', end='')
        print()

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
            if i < 2 and len(liste) >= 2 and liste[0]+liste[1]*10 < 20 and not unities:
                    chaine.insert(0, self.unities[liste[0]+liste[1]*10])
                    unities = True
            elif i == 0 and not unities:
                if i < len(liste)-1 and liste[i] != 0:
                    chaine.insert(0, self.unities[liste[i]])
                elif len(liste) == 1:
                    chaine.insert(0, self.unities[liste[i]])
            elif i == 1 and not unities:
                if liste[i-1] != 0:
                    chaine.insert(0, '-')
                chaine.insert(0, self.tens[liste[i]-1])
            elif i == 2:
                chaine.insert(0, self.unities[liste[i]] + ' ' + self.hundred[0] + ' and ')
            elif i == 3 and i < len(liste)-1 and liste[i]+liste[i+1]*10 < 20 and not thousands:
                chaine.insert(0, self.unities[liste[i]+liste[i+1]*10] + ' ' + self.thousand[0] + ' and ')
                thousands = True
            elif i == 3 and not thousands:
                chaine.insert(0, self.unities[liste[i]] + ' ' + self.thousand[0] + ' and ')
            elif i > 2 and not thousands:
                chaine.insert(0, self.tens[liste[i]])
        # print(f'{chaine}')
        for i in chaine:
            print(i, end='')
        print()


if __name__ == '__main__':
    starttime = time.time()
    # main(1000)
    n = Nombre()
    n.Décomposer(100)
    n.Décomposer(1000)
    # for x in range(101):
    #     print(f'{x} : ', end='')
    #     n.Décomposer(x)
    print(f'Durée d\'exécution : {time.time()-starttime}s.')