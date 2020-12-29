# coding utf-8

f = 1
for i in range(1,101):
    # print(f'{i}x{f}', end='')
    f *= i
    # print(f'={f}')

string = str(f)
sum = int()
for i in string:
    # print(i)
    sum += int(i)

print(sum)