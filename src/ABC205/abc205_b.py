def run(n):
    a = list(map(int, input().split()))
    if len(list(set(a))) == n:
        print('Yes')
    else:
        print('No')
    


if __name__ == '__main__':
    n = int(input())
    run(n)