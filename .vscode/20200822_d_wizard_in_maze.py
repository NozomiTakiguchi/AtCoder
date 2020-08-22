def run(h, w, ch, cw, dh, dw, _in):
    '''
    see. https://atcoder.jp/contests/abc176/tasks/abc176_d

    → TODO 解説確認. 幅優先探索を使って、全ての到達可能なマスに対してその移動コストを算出する

    '''
    horiz_steps = abs(dh - ch)
    vert_steps = abs(dw - cw)

    cast_count = 0

    _available_list = []

    # 現在地点から移動可能な箇所を洗い出そうとした
    def _available(current_h, current_w, maze):
        if current_w + 1 <= w:
            if maze[current_h-1][current_w] != '#':
                _available_list.append([current_h, current_w+1])
        if current_w - 1 > 0:
            if maze[current_h-1][current_w-2] != '#':
                _available_list.append([current_h, current_w-1])
        if current_h + 1 <= h:
            if maze[current_h][current_w-1] != '#':
                _available_list.append([current_h+1, current_w])
        if current_h - 1 > 0:
            if maze[current_h-2][current_w-1] != '#':
                _available_list.append([current_h-1, current_w])
        return _available_list
    
    _available_list = _available(ch, cw, _in)
    print(_available_list)

if __name__ == '__main__':
    h, w= list(map(int, input().split()))
    ch, cw = list(map(int, input().split()))
    dh, dw = list(map(int, input().split()))
    _in = [[c for c in input().strip()] for _ in range(w)]
    run(h, w, ch, cw, dh, dw, _in)