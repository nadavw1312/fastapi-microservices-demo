from sqlalchemy.ext.asyncio import  AsyncSession
from src.user.user_api_schemas import UserCreate, UserResponse
from src.user.user_dal import add_user, fetch_user


async def create_user(session: AsyncSession,user: UserCreate) -> UserResponse:
    _user = await add_user(session,user)
    return UserResponse(id=_user.id, name=user.name, email=user.email,newProp=user.newProp)

async def get_user(session: AsyncSession,user_id: int) -> UserResponse:
    user = await fetch_user(session,user_id)
    if user:
        return UserResponse(id=user.id, name=user.name, email=user.email,newProp=user.newProp)
    raise Exception("User not found")
