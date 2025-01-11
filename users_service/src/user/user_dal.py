from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from src.user.user_api_schemas import UserCreate
from src.user.user_models import User

# Add user to the database
async def add_user(session: AsyncSession,user: UserCreate) -> User:
    db_user = User(name=user.name, email=user.email, password=user.password, newProp=user.newProp)
    session.add(db_user)
    await session.commit()  # Use await for async commit
    await session.refresh(db_user)  # Use await for async refresh
    
    return db_user  # Access the actual value of the id column

# Fetch user from the database
async def fetch_user(session: AsyncSession,user_id: int) -> Optional[User]:
    result = await session.execute(
        select(User).filter(User.id == user_id)
    )
    return result.scalars().first()
