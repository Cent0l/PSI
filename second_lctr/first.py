import aiohttp
import asyncio

async def fetch(url: str) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()


async def main() -> None:
    url = "https://httpbin.org/get"
    data = await fetch(url)
    print(data)


if __name__ == "__main__":
    asyncio.run(main())