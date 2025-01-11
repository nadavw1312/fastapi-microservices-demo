# from fastapi import FastAPI, Request
# from contextvars import ContextVar
# from sqlalchemy.ext.asyncio import AsyncSession
# from users_service.db.database import create_session

# app = FastAPI()

# db_session: ContextVar[AsyncSession] = ContextVar('db_session')

# @app.middleware('http')
# async def db_session_middleware(request: Request, call_next):
#     session = create_session()
#     token = db_session.set(session)
#     try:
#         response = await call_next(request)
#     finally:
#         db_session.reset(token)
#         await session.close()
#     return response

