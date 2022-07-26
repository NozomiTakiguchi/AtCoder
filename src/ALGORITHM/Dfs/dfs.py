# https://qiita.com/keisuke-ota/items/6c1b4846b82f548b5dec

class Node:
    def __init__(self, index) -> None:
        self.index = index
        self.neighbors  = []
        self.sign = False

