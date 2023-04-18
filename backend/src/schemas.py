import datetime

from pydantic import BaseModel

from backend.database.models import SearchEngineType


class CreateCollectorInput(BaseModel):
    name: str = None
    description: str = None
    search_query: str
    search_engine: str
    num_images: int
    max_time_s: int = None
    status: str


class CreateCollectorResponse(BaseModel):
    id: int


class CollectorResponse(BaseModel):
    id: int
    name: str = None
    description: str = None
    search_query: str
    search_engine: SearchEngineType
    num_images: int
    max_time_s: int
    created_at: datetime.datetime


class CollectorsData(BaseModel):
    jobs: list[CollectorResponse] = []
