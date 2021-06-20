def run(s):
    '''

    '''
    print('{}{}'.format(s, 'es' if s[-1] == 's' else 's'))

if __name__ == '__main__':
    s = input()

    run(s)