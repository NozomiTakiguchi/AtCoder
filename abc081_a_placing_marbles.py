def run():
    '''
    0 と 1 のみから成る n 桁の番号 s が与えられます。1 が何個含まれるかを求めてください。
    '''
    a = input()
    _in = [int(i) for i in list(a) if int(i) == 1]
    print('input array of number is {}, in which 1 appears {} times.'.format(a, len(_in)))
    

if __name__ == '__main__':
    run()