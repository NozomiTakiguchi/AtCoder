def run(a, b):
    print(a*(b/100))
    


if __name__ == '__main__':
    a,b  = map(int, input().split())
    run(a, b)