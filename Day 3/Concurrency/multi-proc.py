import time
from concurrent.futures import ProcessPoolExecutor

def square_number(n):
    """Simulate CPU-heavy work by squaring a number."""
    print(f"Processing {n}...")
    result = n * n
    return result

def main():
    numbers = [1, 2, 3, 4, 5]  # simple numbers
    start = time.perf_counter()

    # Use multiprocessing: 2 processes
    with ProcessPoolExecutor(max_workers=2) as executor:
        results = list(executor.map(square_number, numbers))

    end = time.perf_counter()
    print(f"Results: {results}")
    print(f"Time taken: {end - start:.2f} seconds")

if __name__ == "__main__":
    main()