from fastapi import APIRouter, Depends
from users_service.api.users_api_schemas import UserCreate, UserResponse
from users_service.bl.users_bl import create_user, get_user
from sqlalchemy.ext.asyncio import AsyncSession
from users_service.db.database import get_db_session



router = APIRouter()

@router.post("/", response_model=UserResponse)
async def create_user_endpoint(user: UserCreate,db_session: AsyncSession = Depends(get_db_session) ):
    return await create_user(db_session,user)

@router.get("/{user_id}", response_model=UserResponse)
async def get_user_endpoint(user_id: int,db_session: AsyncSession = Depends(get_db_session) ):
    return await get_user(db_session,user_id)
