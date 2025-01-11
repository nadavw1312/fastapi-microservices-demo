# declarative base from previous example
from typing import Annotated
from sqlalchemy.orm import DeclarativeBase,declarative_base
from sqlalchemy import String
from sqlalchemy.orm import mapped_column


STR50 = Annotated[str, 50]
# expected to be used in multiple places
INTPK = Annotated[int, mapped_column(primary_key=True)]

# Base class for all database models
Base = declarative_base()

