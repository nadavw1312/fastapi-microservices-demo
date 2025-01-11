from asyncio import current_task
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import AsyncEngine
from typing import AsyncGenerator
import logging

from users_service.config import DATABASE_URL
from users_service.db.model import Base

logger = logging.getLogger(__name__)


class DatabaseSessionManager:
    def __init__(self):
        self.engine: AsyncEngine
        self.session_maker = None

    async def init_db(self):
            try:
                # Ensure DATABASE_URL is a string
                if not isinstance(DATABASE_URL, str):
                    raise ValueError("DATABASE_URL must be a string")
                logger.info(f"Initializing database with URL: {DATABASE_URL}")
                
                if "asyncpg" not in DATABASE_URL:
                    raise ValueError("DATABASE_URL must use the 'asyncpg' driver for async support.")
                
                self.engine = create_async_engine(
                    DATABASE_URL, echo=True, pool_size=100, max_overflow=0, pool_pre_ping=True
                )
                self.session_maker = async_sessionmaker(
                    self.engine, expire_on_commit=False
                )
                
                # Use run_sync to create tables
                async def create_tables():
                    async with self.engine.begin() as conn:
                        await conn.run_sync(Base.metadata.create_all)
                        logger.info("Create Database tables")
                        
                

                await create_tables()
                logger.info("Database initialized successfully.")
            except Exception as e:
                logger.error(f"Failed to initialize the database: {e}")
                raise

    async def close(self):
        # Dispose of the engine
        if self.engine is not None:
            await self.engine.dispose()
        else:
            raise Exception("Database engine is not initialized")

# Initialize the DatabaseSessionManager
DB_MANAGER = DatabaseSessionManager()

# Dependency to get a database session
async def get_db_session() -> AsyncGenerator[AsyncSession, None]:
    if DB_MANAGER.session_maker is None:
        raise Exception("DatabaseSessionManager is not initialized")
    async with DB_MANAGER.session_maker() as session:
        try:
            yield session
        except Exception as e:
            await session.rollback()
            logger.error(f"Database error: {e}")
            raise
        finally:
            await session.close()
