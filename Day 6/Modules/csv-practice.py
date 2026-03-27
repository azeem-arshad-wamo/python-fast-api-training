import csv

def generator():
    with open("../../Project/Data/large_test.csv", "r") as f:
        reader = csv.DictReader(f)
    
        for row in reader:
            yield row


gen = generator()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
