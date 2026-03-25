import asyncio

async def fetch_data(task_name):
    print(f"Starting {task_name}")
    await asyncio.sleep(2)  # NON-BLOCKING
    print(f"Finished {task_name}")

async def main():
    tasks = [
        fetch_data("Task-1"),
        fetch_data("Task-2"),
        fetch_data("Task-3")
    ]
    await asyncio.gather(*tasks)

asyncio.run(main())

import asyncio

# Async function to simulate fetching data from an API
async def fetch_data(name, delay):
    print(f"Fetching {name}...")
    await asyncio.sleep(delay)  # simulates network delay
    print(f"Finished fetching {name}")
    return f"Data from {name}"

# Main async function
async def main():
    # List of “API calls” to make
    tasks = [
        fetch_data("API 1", 2),
        fetch_data("API 2", 3),
        fetch_data("API 3", 1)
    ]
    
    # Run all tasks concurrently
    results = await asyncio.gather(*tasks)
    print("All results:", results)

# Run the event loop
asyncio.run(main())