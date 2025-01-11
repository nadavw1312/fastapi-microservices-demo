from logging.config import fileConfig
from sqlalchemy import pool
from sqlalchemy.ext.asyncio import AsyncEngine
from alembic import context
from users_service.dal.user_models import Base
from users_service.db.database import DB_MANAGER
import logging
import asyncio

config = context.config

# Check if config_file_name is not None
if config.config_file_name is not None:
    fileConfig(config.config_file_name)
else:
    # Provide a default logging configuration
    logging.basicConfig(level=logging.INFO)
    logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

target_metadata = Base.metadata

async def run_migrations_online():
    # Initialize the database engine
    try:
        await DB_MANAGER.init_db()
        logging.info("Database engine initialized successfully.")
    except Exception as e:
        logging.error(f"Failed to initialize the database engine: {e}")
        return
    
    connectable = DB_MANAGER.engine

    if connectable is None:
        logging.error("Database engine is None after initialization.")
        return

    async def do_migrations():
        async with connectable.connect() as connection:
            await connection.run_sync(run_migrations)

    def run_migrations(connection):
        context.configure(connection=connection, target_metadata=target_metadata)
        with context.begin_transaction():
            context.run_migrations()


    await do_migrations()

asyncio.run(run_migrations_online())
