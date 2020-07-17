import asyncio

#sleep for a second and then generate a square
async def square_number(x):
    print(f"going to sleep with input {x}")
    await asyncio.sleep(1)
    print(f"awake with number {x}")
    return x**2

loop = asyncio.get_event_loop()
future = loop.create_task(square_number(5))
results = loop.run_until_complete(future)
print(results)
loop.close()

