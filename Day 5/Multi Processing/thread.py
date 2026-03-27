import threading

n = 5
lock = threading.Lock()

def first():
    global n
    with lock:
        n = n + 5

def second():
    global n
    with lock:
        n = n + 5

t1 = threading.Thread(target=first)
t2 = threading.Thread(target=second)

t1.start()
t2.start()

t1.join()
t2.join()

print(n)