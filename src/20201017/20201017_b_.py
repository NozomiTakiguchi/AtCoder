import math
def run(n, _in):
    '''
    '''
    print(sum([abs(i) for i in _in]))
    print(math.sqrt(sum(abs(i)**2 for i in _in)))
    print(sorted([abs(i) for i in _in])[-1])




if __name__ == '__main__':
    n = int(input())
    _in = list(map(int, input().split()))
    run(n, _in)