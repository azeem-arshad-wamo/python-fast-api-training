import multiprocessing

def first(value):
    with value.get_lock():
        value.value += 5

def second(value):
    with value.get_lock():
        value.value += 5

if __name__ == "__main__":
    value = multiprocessing.Value("i", 5)

    p1 = multiprocessing.Process(target=first, args=(value,))
    p2 = multiprocessing.Process(target=second, args=(value,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print(value.value)