import select, socket
from time import time

def slow_systemcall():
    select.select([socket.socket()], [], [], 0.1) # select : I/O 処理の完了を待機する

start = time()
for _ in range(10):
    slow_systemcall()
end = time()

print(F'slow_systemcall. Took {end-start} seconds')