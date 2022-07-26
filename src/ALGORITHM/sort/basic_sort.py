
'''
バブルソート
隣り合う要素を大証比較するソートアルゴリズム
'''
def bubble_sort(arr):
    change = True
    while change:
        change = False
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                change = True
    return arr

'''
選択ソート
徐々に検索レンジを狭めていきながら、そのレンジの中の最小値を list に append するソートアルゴリズム
'''
def sellect_sort(arr):
    for ind, ele in enumerate(arr):
        min_ind = min(range(ind, len(arr)), key=arr.__getitem__)
        arr[ind], arr[min_ind] = arr[min_ind], ele
    return arr

'''
マージソート
半分ずつに再帰的に分割していき、隣り合う要素と大証比較しながらマージを繰り返していくソートアルゴリズム
'''
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    # ここで分割を行う
    left = arr[:mid]
    right = arr[mid:]
    print(left,right, arr)

    # 再帰的に分割を行う
    left = merge_sort(left)
    right = merge_sort(right)

    def _merge(left, right):
        # print(left,right)
        merged = []
        l_i, r_i = 0, 0

        # ソート済み配列をマージするため、それぞれ左から見ていくだけで良い
        while l_i < len(left) and r_i < len(right):
            # ここで=をつけることで安定性を保っている
            if left[l_i] <= right[r_i]:
                merged.append(left[l_i])
                l_i += 1
            else:
                merged.append(right[r_i])
                r_i += 1

        # 上のwhile文のどちらかがFalseになった場合終了するため、あまりをextendする
        if l_i < len(left):
            merged.extend(left[l_i:])
        if r_i < len(right):
            merged.extend(right[r_i:])
        return merged

    # returnが返ってきたら、結合を行い、結合したものを次に渡す
    return _merge(left, right)

'''
クイックソート
pivot (ref のところ) がうまく、 left と right が分割できるような値であれば最良で nlogn の計算量でソートできる

'''
def quick_sort(arr):
    left = []
    right = []
    if len(arr) <= 1:
        return arr

    # データの状態に左右されないためにrandom.choice()を用いることもある。
    # ref = random.choice(arr)
    ref = arr[0]
    ref_count = 0

    for ele in arr:
        if ele < ref:
            left.append(ele)
        elif ele > ref:
            right.append(ele)
        else:
            ref_count += 1 # ref と同じ値の場合インクリメント
    left = quick_sort(left)
    right = quick_sort(right)
    return left + [ref] * ref_count + right

'''
カウントソート
要素の個数を数え上げていく方法. 要素の値を list のインデックスで表し、そのインデックスの値を個数とする
e.g. [3,4,1,3,4] をカウントソートする => [1,0,2,2] と各要素の個数を list 化して
'''
def count_sort(arr):
    max_num = max(arr)
    min_num = min(arr)
    count = [0] * (max_num - min_num + 1)
    for ele in arr:
        count[ele - min_num] += 1
    

    for idx, ele in enumerate(count, start=min_num):
        print(idx, ele)

    # インデックスが欲しいのでわざと ele と cnt 入れ替えている
    return [ele for ele, cnt in enumerate(count, start=min_num) for __ in range(cnt)]

if __name__ == '__main__':
    arr = list(map(int, input().split()))
    # sorted_arr = bubble_sort(arr)
    # sorted_arr = sellect_sort(arr)
    # merged_arr = merge_sort(arr)
    # quick_arr = quick_sort(arr)
    count_arr = count_sort(arr)
    print(count_arr)