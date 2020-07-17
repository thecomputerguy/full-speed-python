import asyncio

#async function with event loop
async def async_function():
    await asyncio.sleep(1)
    print("I am awake!")
    return

#create new event loop, submit a coroutine, get back future and submit future to event loop for
#execution until it's complete
loop = asyncio.new_event_loop()
future = loop.create_task(async_function())
loop.run_until_complete(future)
loop.close()

#Another async function with event loop
async def another_async_function():
    await asyncio.sleep(2)
    print(f"Dude! you gotta be kidding me! This is low level async programming. you gotta do better!")
    return

loop = asyncio.new_event_loop()
future = loop.create_task(another_async_function())
loop.run_until_complete(future)
loop.close()


#Another async function with get_event_loop instead of new_event_loop
async def async_with_get_event_loop():
    await asyncio.sleep(1)
    print(f"Dude! I am awake!")
    return

#get an event loop and submit coroutine to the event loop
loop = asyncio.get_event_loop()
future = loop.create_task(async_with_get_event_loop())
loop.run_until_complete(future)
loop.close()