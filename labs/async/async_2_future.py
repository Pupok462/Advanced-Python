import asyncio


async def set_after(delay, value):
    await asyncio.sleep(delay)
    return value


async def main():

    fut = asyncio.ensure_future(
        set_after(1, '... world'))

    print('hello ...')

    await asyncio.wait_for(fut, None)
    print(fut.result())

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
