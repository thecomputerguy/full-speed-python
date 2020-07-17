import asyncio

async def cube(x):
    print(f"cube async function start")
    await asyncio.sleep(2)
    print(f"cube async function ends")
    return x**3

loop = asyncio.get_event_loop()
results = loop.run_until_complete(asyncio.gather(cube(3), cube(4), cube(5)))
print(results)
loop.close()