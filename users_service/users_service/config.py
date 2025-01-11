from decouple import config

# General Config
APP_NAME = config("APP_NAME", default="users_service")
DEBUG = config("DEBUG", default=False, cast=bool)

# Database Config
DATABASE_URL = config("DATABASE_URL", default="postgresql+asyncpg://users_user:users_password@users-db-dev:5432/users_db")

# RabbitMQ Config
RABBITMQ_HOST = config("RABBITMQ_HOST", default="rabbitmq")
RABBITMQ_USER = config("RABBITMQ_USER", default="user")
RABBITMQ_PASSWORD = config("RABBITMQ_PASSWORD", default="password")

# Posts Microservice Config
POSTS_SERVICE_URL = config("POSTS_SERVICE_URL", default="http://posts-service:8000")

