import itertools
def run(n, k, transit):
    '''

    '''
    cities_list = [i+1 for i in range(1, n)]
    p = itertools.permutations(cities_list, n-1)
    count = 0
    #v は tuple
    for v in p:
        current_city = 1
        all_time = 0
        for city in v:
            # print('current: {} / to: {}'.format(current_city, city))
            all_time += transit[current_city - 1][city - 1]
            current_city = city
        all_time += transit[current_city - 1][0]
        if all_time == k:
            count += 1

    print(count)
if __name__ == '__main__':
    n, k = map(int, input().split())
    transit = [list(map(int, input().split())) for _ in range(n)]
    run(n, k, transit)