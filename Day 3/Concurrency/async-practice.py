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