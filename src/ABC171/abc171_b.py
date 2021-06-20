import time
def run(n, k, num_array):
    '''
    '''
    print(sum([i for i in sorted(num_array)[:k]]))

if __name__ == '__main__':
    n, k = list(map(int, input().split()))
    num_array = list(map(int, input().split()))

    run(n, k, num_array)