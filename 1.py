# coding utf-8
import time

start_time = time.time()
sum = 0
for i in range(1000):
    if i%3 == 0:
        print(f'{i} est multiple de 3')
        sum += i
    elif i%5 == 0:
        print(f'{i} est multiple de 5')
        sum += i

print(f'Somme={sum} ')

print(f'Durée d\'exécution = {time.time()-start_time}s ')
