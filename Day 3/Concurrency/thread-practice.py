import time
import threading

def fetch_data(task_name):
    print(f"Starting {task_name}")
    time.sleep(2)
    print(f"Finished {task_name}")

def main():
    tasks = ["API-1", "API-2", "API-3"]

    start = time.perf_counter()

    threads = []

    for task in tasks:
        t = threading.Thread(target=fetch_data, args=(task,))
        threads.append(t)
        t.start()   # start thread

    for t in threads:
        print(f"Thead: {t}")
        t.join()    # wait for thread to finish

    end = time.perf_counter()

    print(f"Time taken: {end - start:.2f} seconds")

if __name__ == "__main__":
    main()