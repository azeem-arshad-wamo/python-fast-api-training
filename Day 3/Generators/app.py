# We use generators to yield values. They produce values
def myGenerator():
    print("Start")
    yield 1
    print("Next")
    yield 2
    print("End")
    yield 3

gen = myGenerator()
print(next(gen))
print(next(gen))
print(next(gen))

# Yield can also receive values from the outside
def accumulator():
    total = 0
    while True:
        x = yield total
        if x is None:
            break
        total += x

gen = accumulator()
print(next(gen))       # 0
print(gen.send(5))     # 5
print(gen.send(10))    # 15

# We can close a generator manually by using .close() method
gen.close()
