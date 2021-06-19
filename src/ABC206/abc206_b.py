MAX = (10**9)+10
def run(n):
    savings = 0
    # while のほうが効率的ではある
    for i in range(MAX):
        savings += i+1
        if savings >= n:
            print(i+1)
            exit()


if __name__ == '__main__':
    n = int(input())
    run(n)