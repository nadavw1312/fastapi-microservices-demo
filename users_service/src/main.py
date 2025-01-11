import os
import logging
from contextlib import asynccontextmanager
from fastapi import FastAPI
from src.api.middlewares.error_handler_middleware import ErrorHandlerMiddleware
from src.db.database import DB_MANAGER
from src.user import user_api


# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Import debugpy and configure it
if os.getenv("DEBUGPY_ENABLE", "false").lower() == "true":
    import debugpy
    debugpy.listen(("0.0.0.0", 5678))
    logger.info("Debugpy is listening on 0.0.0.0:5678")
    # Uncomment the next line if you want the app to wait until a debugger attaches
    # debugpy.wait_for_client()

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup logic
    await DB_MANAGER.init_db()
    logger.info("Database initialized")

    yield  # Application runs here

    # Shutdown logic
    await DB_MANAGER.close()
    logger.info("Database connection closed")

# Create the FastAPI app with lifespan events
app = FastAPI(
    title="Users Service",
    description="Service for managing users in the system",
    version="1.0.0",
    lifespan=lifespan
)

# Add the error handler middleware
app.add_middleware(ErrorHandlerMiddleware)

# Include API routes
app.include_router(user_api.router, prefix="/users", tags=["Users"])

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Users Service!!"}
