import prisma
import asyncio

class Client:
    async def validate_client(self):
        if not hasattr(prisma, 'Client'):
            process = await asyncio.create_subprocess_exec('prisma', 'db', 'push')
            await process.wait()
        self.db = prisma.Client(datasource={'url': 'file:./ponydb.sqlite'}, auto_register=True)
            
    async def connect(self):
        await self.validate_client()
        await self.db.connect()

    async def disconnect(self):
        await self.db.disconnect()

    async def __aenter__(self):
        await self.connect()
        return self

    async def __aexit__(self, *_):
        await self.disconnect()

    async def test(self) -> None:
        from prisma.models import characters
        ponies = await characters.prisma().find_many(where={"CharacterID": 2})
        print(ponies)

async def main():
    async with Client() as c:
        await c.test()

asyncio.run(main())
