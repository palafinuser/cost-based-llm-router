from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from collections.abc import Generator

from llm_router.config import settings

engine = create_engine(
    settings.database_url,
    echo = True,    #logging reasons (dev)
    pool_pre_ping = True,   #prevent stale connections
)

SessionLocal = sessionmaker(
    bind = engine,
    autoflush = False,
    expire_on_commit = False,
)

def get_db() -> Generator[Session, None, None]:
    with SessionLocal() as session:
        yield session