from sqlalchemy import select

from backend.database import models
from backend.src.schemas import CreateCollectorInput


class Database:

    def __init__(self, session_maker):
        print("Created DB!")
        self.session_maker = session_maker

    async def create_collector(self, collector_data: CreateCollectorInput) -> models.Collector:
        async with self.session_maker() as session:
            instance = models.Collector(**collector_data.dict())
            session.add(instance)
            await session.commit()
            await session.refresh(instance)
            await session.close()
            return instance

    async def get_collectors(self) -> list:
        async with self.session_maker() as session:
            collectors = await session.execute(select(models.Collector))
            collectors = collectors.scalars().all()
            return collectors

