
'''
バブルソート
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
'''
def sellect_sort(arr):
    for ind, ele in enumerate(arr):
        min_ind = min(range(ind, len(arr)), key=arr.__getitem__)
        arr[ind], arr[min_ind] = arr[min_ind], ele
    return arr

'''
マージソート  
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


if __name__ == '__main__':
    arr = list(map(int, input().split()))
    # sorted_arr = bubble_sort(arr)
    # sorted_arr = sellect_sort(arr)
    merged_arr = merge_sort(arr)
    print(merged_arr)