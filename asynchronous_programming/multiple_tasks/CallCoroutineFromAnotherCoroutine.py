import asyncio

#main coroutine
async def compute_cube(x):
    print(f"compute_cube coroutine started")
    await asyncio.sleep(2)
    print(f"computer_cube coroutine finished")
    return x**3

#calls another coroutine
async def cube(x):
    print(f"cube coroutine started")
    result = await compute_cube(x)
    print(f"cube coroutine finished")
    return result

async def when_done(tasks):
    for task in asyncio.as_completed(tasks):
        print(f"{await task}")

loop = asyncio.get_event_loop()
loop.run_until_complete(when_done([cube(3), cube(4), cube(5)]))
loop.close()