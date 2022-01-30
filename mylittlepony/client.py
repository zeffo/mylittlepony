import prisma
import asyncio

class Client:
    def __init__(self) -> None:
        self.db = prisma.Client(datasource={'url': 'file:./ponydb.sqlite'}, auto_register=True)

    async def connect(self):
        await self.db.connect()

    async def disconnect(self):
        await self.db.disconnect()

    async def __aenter__(self):
        await self.connect()
        return self

    async def __aexit__(self, *_):
        await self.disconnect()

    async def test(self) -> None:
        ponies = await prisma.models.characters.prisma().find_many()
        print(ponies)

async def main():
    async with Client() as c:
        await c.test()

asyncio.run(main())
