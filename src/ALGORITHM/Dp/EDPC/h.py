class Node:
    def __init__(self, index) -> None:
        self.index = index
        pass

def run(h,w,a):
    print(a)

if __name__ == '__main__':
    h,w = map(int, input().split())
    a = [input().split() for _ in range(h)]
    run(h,w,a)