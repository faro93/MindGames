#coding utf-8

sumofsquares = 0
squareofsum = 0

for i in range(101):
    sumofsquares += i**2
    squareofsum += i

squareofsum = squareofsum**2

print(f'{squareofsum}-{sumofsquares}={squareofsum-sumofsquares}')
