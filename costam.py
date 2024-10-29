import asyncio
import aiohttp



@dataclass
class Posts:
    userId: int
    id: int
    title: str
    body: str


class PostsRepozytory():
    async def get_all_posts(self,userId: int) -> Iterable[Posts] | None:
        posts= await self._get_posts(userId)
        parse_post= await self._parse_post(posts)

        return posts


    async def _get_posts(self,userId:int) -> Iterable[dict] | None:
        async with aiohttp.ClientSession() as session:
            async with session.get("https://jsonplaceholder.typicode.com/posts") as response:
                if response.status != 200:
                    return None

                return await response.json()

    async def _parse_post(self, posts: Iterable[dict] ) ->Iterable[Posts]:
        return [Posts(title=recrd.get("title"),body=record.get("body")) for record in posts["lines"]]

















if __name__ == "__main__":
    container = Container()
    container.wire(modules=[__name__])


    asyncio.run(main())



