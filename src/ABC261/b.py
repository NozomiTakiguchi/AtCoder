def run(n, aij):
    for i,e in enumerate(aij):
        for j, ee in enumerate(e):
            if ee == '-':
                continue
            if ee == 'W':
                if aij[j][i] != 'L':
                    print('incorrect')
                    exit()
            elif ee == 'L':
                if aij[j][i] != 'W':
                    print('incorrect')
                    exit()
            else: # D のとき
                if aij[j][i] != 'D':
                    print('incorrect')
                    exit()
    
    print('correct')



if __name__ == '__main__':
    n = int(input())
    aij = [[e for e in input()] for _ in range(n)]
    run(n, aij)