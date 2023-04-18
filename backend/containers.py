from dependency_injector import containers, providers

from backend.config import get_settings
from backend.database.db import Database
from backend.database.connection.session import get_session


class Container(containers.DeclarativeContainer):

    wiring_config = containers.WiringConfiguration(modules=[".src.handlers"])

    # used to store image analysis results
    session_maker = providers.Singleton(
        get_session, get_settings().database_uri)
    database = providers.Singleton(Database, session_maker)
