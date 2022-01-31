from .prisma import client

class Client:
    def __init__(self):
        root = "\\".join(__file__.split("\\")[:-1])  
        self.db = client.Client(datasource={'url': f'file:{root}\\db.sqlite'}, auto_register=True)
            
    async def connect(self):
        await self.db.connect()

    async def disconnect(self):
        await self.db.disconnect()

    async def __aenter__(self):
        await self.connect()
        return self

    async def __aexit__(self, *_):
        await self.disconnect()

    @property
    def query(self) -> client.Client:
        return self.db