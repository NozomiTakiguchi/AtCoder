import numpy as np
def run(n, a):
    '''

    '''
    a1, a2 = np.array_split(a, 2)
    a1 = a1.tolist()
    a2 = a2.tolist()
    a1_m = max(a1)
    a2_m = max(a2)

    print(a1.index(a1_m)+1 if a1_m < a2_m else len(a1)+a2.index(a2_m) + 1)



if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    run(n, a)