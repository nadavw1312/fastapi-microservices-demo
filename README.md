# Users Service

This is a FastAPI-based microservice for managing user data. It includes features for creating, fetching, and updating user information.

## Prerequisites

- **Python 3.12**: Ensure you have Python 3.12 installed on your system.
- **Docker**: Required for running the service in a containerized environment.
- **PostgreSQL**: The service uses PostgreSQL as its database.

## Installation

### Clone the Repository

```

### Set Up the Environment

1. **Create a Virtual Environment**:

   ```bash
   python3.12 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

2. **Install Dependencies**:

   Use `pip` to install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

   Alternatively, if you are using Poetry, you can install dependencies with:

   ```bash
   poetry install
   ```

### Configuration

1. **Environment Variables**:

   Create a `.env` file in the root directory and configure the following variables:

   ```env
   APP_NAME=users_service
   DEBUG=True
   DATABASE_URL=postgresql+asyncpg://users_user:users_password@users-db-dev:5432/users_db
   RABBITMQ_HOST=rabbitmq
   RABBITMQ_USER=user
   RABBITMQ_PASSWORD=password
   POSTS_SERVICE_URL=http://posts-service:8000
   ```

   Refer to the configuration setup in `src/config.py` for more details:

   ```python
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
   ```

### Database Initialization

1. **Run Database Migrations**:

   Use Alembic to apply database migrations:

   ```bash
   alembic upgrade head
   ```

   Ensure your `alembic.ini` and migration scripts are correctly set up.

### Running the Application

1. **Using Uvicorn**:

   Start the application using Uvicorn:

   ```bash
   uvicorn src.main:app --host 0.0.0.0 --port 8000
   ```

   The application will be accessible at `http://localhost:8000`.

2. **Using Docker**:

   Build and run the Docker container:

   ```bash
   docker build -t users-service .
   docker run -p 8000:8000 users-service
   ```

   The Dockerfile is configured to expose the necessary ports:

   ```dockerfile
   FROM python:3.12-slim

   # Set working directory
   WORKDIR /app

   # Copy and install dependencies
   COPY requirements.txt .
   RUN pip install --no-cache-dir -r requirements.txt
   RUN pip install debugpy

   # Copy the application code
   COPY . .

   # Expose necessary ports
   EXPOSE 8000 5678

   # Enable debugpy via environment variable
   ENV DEBUGPY_ENABLE=true

   # Start the application with uvicorn
   CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
   ```

## Development

### Debugging

Debugging is enabled via `debugpy`. Ensure the `DEBUGPY_ENABLE` environment variable is set to `true` to allow remote debugging.

### Code Quality

- **Black**: For code formatting.
- **Flake8**: For linting.
- **Isort**: For sorting imports.

Run these tools to maintain code quality:

```bash
black .
flake8 .
isort .
```

### Testing

Use `pytest` for running tests:

```bash
pytest
```

## API Documentation

Once the application is running, you can access the API documentation at `http://localhost:8000/docs`.

## Contributing

Feel free to submit issues or pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License.