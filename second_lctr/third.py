from asyncio import gather

import aiohttp
import asyncio

async def fetch(url: str) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()


async def page1() -> None:
    url = "https://670bef0e7e5a228ec1cf1824.mockapi.io/api/v1/user"
    data = await fetch(url)
    print(data)

async def page2() -> None:
    url = "https://670bef0e7e5a228ec1cf1824.mockapi.io/api/v1/user"
    data = await fetch(url)
    print(data)

async def page3() -> None:
    url = "https://670bef0e7e5a228ec1cf1824.mockapi.io/api/v1/user"
    data = await fetch(url)
    print(data)

async def page4() -> None:
    url = "https://670bef0e7e5a228ec1cf1824.mockapi.io/api/v1/user"
    data = await fetch(url)
    print(data)

async def page5() -> None:
    url = "https://670bef0e7e5a228ec1cf1824.mockapi.io/api/v1/user"
    data = await fetch(url)
    print(data)
async def pages()->None:
    await asyncio.gather(page1(), page2(), page3(), page4(), page5())

if __name__ == "__main__":
    asyncio.run(pages())

