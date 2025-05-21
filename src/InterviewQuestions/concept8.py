import asyncio
import time


def task(name):
    print(f"starting {name}")
    time.sleep(2)
    print(f"finished {name}")

# task("Rahul")
# task("Shetty")

async def task(name):
    print(f"starting {name}")
    await asyncio.sleep(2)
    print(f"finished {name}")

async def main():
    await asyncio.gather(task("Rahul"),task("Shetty"))

asyncio.run(main())