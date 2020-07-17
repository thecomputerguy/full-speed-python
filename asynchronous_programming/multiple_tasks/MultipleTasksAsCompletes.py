import asyncio

async def square(x):
        print(f"square function started")
        await asyncio.sleep(2)
        print(f"square function finished")
        return x**2

async def when_done(tasks):
    for task in asyncio.as_completed(tasks):
        print(f"Result : {await task}")

#create an event loop, execute tasks in parallel and print result as an individual task completes.
#This does not wait for other tasks to complete
#It prints result as tasks complete
loop = asyncio.get_event_loop()
loop.run_until_complete(when_done([square(2), square(3), square(4)]))
loop.close()