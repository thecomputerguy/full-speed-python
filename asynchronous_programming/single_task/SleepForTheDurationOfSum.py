import asyncio

async def sum_of_two_numbers(x: int, y: int):
    print(f"sum_of_two_numbers started")
    result = x+y
    await asyncio.sleep(result)
    print(f"sum_of_two_numbers finished execution")
    return result

loop = asyncio.get_event_loop()
future = loop.create_task(sum_of_two_numbers(2,3))
result = loop.run_until_complete(future)
print(f"{result}")
loop.close()