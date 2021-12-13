from sqlalchemy.ext.asyncio import create_aync_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base

ASYNC_DB_URL = "mysql+aiomysql://root@db:3306/demo?charset=utf8"

async_engine = create_aync_engine(ASYNC_DB_URL, echo=True)
async_session = sessionmaker(
  autocommit=False, autoflush=False, bind=async_engine, class_=AsyncSession
)

Base = declarative_base()

async def geb_db():
  async with async_session() as session:
    yield session
