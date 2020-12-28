# coding utf-8

from colorama import Fore, Style

leap = False
century = dict()

def IsLeap(year):
    leap = False
    if year%400 == 0:
        # print(f'{year} est une année bissextile.')
        leap = True
    elif year%4 == 0 and year%100 != 0:
        # print(f'{year} est une année bissextile.')
        leap = True
    return(leap)

def main():
    for y in range(1900, 2001):
        leap = IsLeap(y)
        century[y] = list()
        for month in range(1, 13):
            if month in (1, 3, 5, 7, 8, 10, 12):
                century[y].append(31)
            elif month == 2:
                if leap:
                    century[y].append(29)
                else:
                    century[y].append(28)
            else:
                century[y].append(30)

    c = 1
    day2mark = 0
    sundayFirst = 0
    for y in sorted(century.keys()):
        print(y)
        for m in enumerate(century[y]):
            print(f'   {m[0]+1, m[1]} : ', end='')
            for d in range(1, m[1]+1):
                if (c+day2mark)%7 == 0:
                    print(f'{Fore.RED}{d}{Style.RESET_ALL} ', end='')
                    if d == 1 and y != 1900:
                        sundayFirst += 1
                else:
                    print(f'{d} ', end='')
                c += 1
            print()
    
    print(sundayFirst)

    # for i in range(5):
    #     if i%2 == 0:
    #         print(f'{Fore.RED}{i}{Style.RESET_ALL}')
    #     else:
    #         print(i)

if __name__ == '__main__':
    main()
