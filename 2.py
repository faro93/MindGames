# coding utf-8
import time

class enigme2():
    def __init__(self, max):
        print(f'Calcul des n termes de Fibonacci inférieurs à {max}')
        self.first_term = int()
        self.second_term = int()
        self.next_term = int()
        self.sum = int()
        self.result = int()

        c = 2
        while self.next_term <= max:
            if c > 2:
                self.first_term, self.second_term = self.second_term, self.next_term
                self.next_term = self.first_term + self.second_term
            else:
                self.first_term, self.second_term = 1, 2
                self.next_term = self.first_term + self.second_term
            c += 1
            if self.second_term%2 == 0:
                print(f'{self.sum}+{self.second_term}=', end='')
                self.sum += self.second_term
                print(f'{self.sum}')


if __name__ == "__main__":
    start_time = time.time()
    f = enigme2(4_000_000)
    print(f'Durée d\'exécution = {time.time()-start_time}s ')
