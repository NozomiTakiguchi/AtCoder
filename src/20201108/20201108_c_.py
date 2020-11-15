import itertools
import math
def run(n):
    '''

    '''
    num = 0
    for e in str(n):
        num += int(e)
    if num %3 == 0:
        print(0)
        exit()
    
    num_list = [int(e) for e in str(n)]

    if num %3 == 1:
        if len([e for e in num_list if e%3 == 1]) >0:
            print(1)
            exit()
        else:
            if len(num_list) <= 2:
                print(-1)
                exit()
            print(2)
            exit()
    
    else:
        if len([e for e in num_list if e%3 == 2]) >0:
            print(1)
            exit()
        else:
            if len(num_list) <= 2:
                print(-1)
                exit()
            print(2)
            exit()


if __name__ == '__main__':
    n = int(input())
    run(n)