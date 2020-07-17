import asyncio

async def sum_of_two_numbers(x: int, y: int):
    print(f"function started")
    await asyncio.sleep(5)
    print(f"function finished")
    return x+y

loop = asyncio.get_event_loop()
results = loop.run_until_complete(asyncio.gather(sum_of_two_numbers(10,20), sum_of_two_numbers(25,30), sum_of_two_numbers(15,25)))
print(f"Results: {results}")
loop.close()
