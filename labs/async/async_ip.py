from collections import namedtuple
import time
import asyncio
import aiohttp
from aiohttp.client_exceptions import ClientConnectorError

Service = namedtuple('Service', ('name', 'url', 'ip_attr'))

SERVICES = (
    Service('ipify', 'https://api.ipify.org?format=json', 'ip'),
    Service('ip-api', 'https://ip-api.com/json', 'query')
)


async def fetch_ip(service):
    try:
        print(f"Try connect to {service.url}")
        async with aiohttp.ClientSession() as session:
            async with session.get(service.url) as resp:
                text = await resp.json()
                print(text)
    except ClientConnectorError:
        print(f"URL address {service.url} is incorrect")


async def asynchronous(runtime: time):
    task_1 = asyncio.create_task(fetch_ip(SERVICES[0]))
    task_2 = asyncio.create_task(fetch_ip(SERVICES[1]))
    tasks = [task_1, task_2]
    await asyncio.wait(tasks, timeout=runtime, return_when=asyncio.ALL_COMPLETED)


ioloop = asyncio.get_event_loop()
ioloop.run_until_complete(asynchronous(2))
