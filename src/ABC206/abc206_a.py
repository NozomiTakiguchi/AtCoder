from math import modf

if __name__ == '__main__':
    n = int(input())

    _, a = modf(n*1.08)
    if int(a) < 206:
        print('Yay!')
    elif int(a) == 206:
        print('so-so')
    else:
        print(':(')