import asyncio
from dataclasses import dataclass
from typing import Optional
import aiohttp
from loguru import logger


@dataclass
class Service:
    name: str
    url: str
    field: str


SERVICES = [
    Service(name="ipify", url="https://api.ipify.org/?format=json", field="ip"),
    Service(name="ip-api", url="http://ip-api.com/json", field="query"),
]

async def fetch_json(session: aiohttp.ClientSession, url: str) -> dict:
    async with session.get(url) as response:
        data: dict = await response.json()
        logger.info("got response for {} with status {} and data {}", url, response.status, data)
        return data


async def fetch_ip(service: Service) -> Optional[str]:
    logger.info("fetch ip from {!r}", service.name)

    async with aiohttp.ClientSession() as session:
        data = await fetch_json(session, service.url)
        return data.get(service.field)


async def get_my_ip(timeout=0.5) -> str:
    logger.info("searching for ip")
    tasks = {
        asyncio.create_task(fetch_ip(service), name=service.name)
        for service in SERVICES
    }
    coro = asyncio.wait(
        tasks,
        timeout=timeout,
        return_when=asyncio.ALL_COMPLETED,
    )
    done, pending = await coro

    for task in pending:  # type: asyncio.Task
        task.cancel()
        logger.info("Cancelled task {}", task)

    my_ip = ""
    for task in done:
        my_ip = task.result()
        break
    else:
        logger.warning("Could not fetch IP!")

    logger.info("Finishing with IP {!r}", my_ip)
    return my_ip


if __name__ == '__main__':
    ip = asyncio.run(get_my_ip(timeout=0.15))
    logger.info("done, ip {!r}", ip)