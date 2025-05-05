from sqlalchemy.ext.asyncio import create_async_engine,AsyncSession
from sqlalchemy.orm import sessionmaker,declarative_base
from backend.config import DATABASE_URL

engine = create_async_engine(DATABASE_URL,echo=True)

SessionLocal = sessionmaker(bind = engine, class_=AsyncSession , expire_on_commit = False)

Base = declarative_base()