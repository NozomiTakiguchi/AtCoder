import math

ni = lambda: int(_n())
na = lambda: list(map(int, input().split()))
_n = lambda: input()

def run():
    p = ni()
    coins = [math.factorial(i+1) for i in range(10)]

    ans = 0
    for i in coins[::-1]:
        while p - i >= 0:
            p -= i
            ans += 1
    
    print(ans)


if __name__ == '__main__':
    run()