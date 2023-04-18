from fastapi import APIRouter, Depends
from dependency_injector.wiring import Provide, inject
from starlette.status import HTTP_200_OK
from starlette.responses import Response

from backend import logger
from backend.containers import Container
from backend.database.db import Database
from backend.logger import get_logger
from backend.src.schemas import CreateCollectorInput, CreateCollectorResponse, CollectorResponse, CollectorsData

router = APIRouter()

logger = get_logger(__name__)


@router.get("/status")
def health_check():
    return Response(status_code=HTTP_200_OK)


@router.post("/collectors")
@inject
async def post_collector(search_query: str,
                         search_engine: str,
                         num_images: int,
                         name: str = " ",
                         description: str = " ",
                         max_time_s: int = 0,
                         status: str = "accepted",
                         db: Database = Depends(Provide[Container.database])):
    collector_data = CreateCollectorInput(name=name,
                                          description=description,
                                          max_time_s=max_time_s,
                                          search_engine=search_engine,
                                          search_query=search_query,
                                          num_images=num_images,
                                          status=status)
    logger.info(f"Received collector data {collector_data.__dict__}")
    collector_instance = await db.create_collector(collector_data)
    logger.info(f"Saved collector data {collector_instance.__dict__}")
    return CreateCollectorResponse(id=collector_instance.id)


@router.get("/collectors")
@inject
async def get_collectors(db: Database = Depends(Provide[Container.database])):
    collectors_instances = await db.get_collectors()
    collectors = [CollectorResponse(**instance.__dict__) for instance in collectors_instances]
    return CollectorsData(jobs=collectors)
