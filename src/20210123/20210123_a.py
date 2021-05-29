def run(n):
    '''

    '''
    if len(set(n)) == 1:
        print('Won')
    else:
        print('Lost')


if __name__ == '__main__':
    n = input()

    run(n)