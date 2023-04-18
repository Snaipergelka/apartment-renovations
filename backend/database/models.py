import enum
from sqlalchemy import Column, String, Integer, Enum, TIMESTAMP, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class StatusType(enum.Enum):
    accepted = "accepted"
    processing = "processing"
    error = "error"
    finished = "finished"


class SearchEngineType(enum.Enum):
    google = "google"


class StorageType(enum.Enum):
    aws = "aws"


class Collector(Base):
    __tablename__ = "collectors"

    id = Column("Collector id", Integer, primary_key=True)
    name = Column("Collector name", String(200))
    description = Column("Collector description", String(200))
    status = Column("Downloading status", Enum(StatusType))
    search_engine = Column("Image search engine", Enum(SearchEngineType))
    num_images = Column("Total number of images to download", Integer)
    storage = Column("Image storage", Enum(StorageType))
    search_query = Column("Search query", String(100))
    max_time_s = Column("Maximum time to collect images", Integer)
    created_at = Column("Created at", TIMESTAMP, server_default=func.now())

    def __str__(self):
        return self.id

    def save(self):
        if not self.name:
            self.name = f"Collector {self.id}"


class ImageCounter(Base):
    __tablename__ = "collector_counters"

    id = Column("Counter id", Integer, primary_key=True)
