import aiohttp
import asyncio

async def fetch(url: str) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()


async def main() -> None:
    url = "https://api.open-meteo.com/v1/forecast?latitude=49.17&longitude=19.58&current=temperature_2m"
    weather = await fetch(url)
    print(weather)


if __name__ == "__main__":
    asyncio.run(main())