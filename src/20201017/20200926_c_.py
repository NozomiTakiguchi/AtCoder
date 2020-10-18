import itertools
def run(_n):
    def make_divisors(n):
        divisors = []
        for i in range(1, int(n**0.5)+1):
            if n % i == 0:
                divisors.append(i)
                if i != n // i:
                    divisors.append(n//i)

        divisors.sort()
        return divisors
    for i in make_divisors(_n):
        print(i)

if __name__ == '__main__':
    n = int(input())

    run(n)
