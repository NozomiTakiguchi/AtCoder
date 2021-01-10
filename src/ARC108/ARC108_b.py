import itertools
def run(n, s):
    '''

    '''
    # while 'fox' in s:
    #     s = s.replace('fox', '')
    # print(len(s))
    _list = [False]*2*10**5
    for i, e in enumerate(s):
        if _list[i]:
            continue
        if e == 'f':
            if i >= len(e) - 2:
                continue
            if s[i+1] != 'o':
                continue
            _list[i+1] = True
            if s[i+2] != 'x':
                continue
            _list[i+2] = True
        elif e == 'o':




if __name__ == '__main__':
    n = int(input())
    s = input()

    run(n, s)