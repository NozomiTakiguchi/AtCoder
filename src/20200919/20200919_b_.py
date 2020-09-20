def run(n, _in_list):
    '''
    '''
    is_doublet_count = 0
    for x in _in_list:
        if is_doublet_count == 3:
            break
        _in = list(x)
        if _in[0] ==_in[1]:
            is_doublet_count += 1
        else:
            is_doublet_count = 0
    
    print('Yes' if is_doublet_count >= 3 else 'No')
    




if __name__ == '__main__':
    n = int(input())
    _in_list = [map(int, input().split()) for _ in range(n)]
    run(n, _in_list)