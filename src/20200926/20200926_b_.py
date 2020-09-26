def run(_in_list):
    '''
    '''
    a = _in_list[0]
    b = _in_list[1]
    c = _in_list[2]
    d = _in_list[3]

    if b < c or d < a:
        print('No')
    else:
        print('Yes')
    




if __name__ == '__main__':
    _in_list = list(map(int, input().split()))
    run(_in_list)